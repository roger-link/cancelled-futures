export async function mountWave() {

    const [THREE, { EffectComposer }, { RenderPass }, { UnrealBloomPass }, { ShaderPass }] = await Promise.all([
      import("three"),
      import("three/addons/postprocessing/EffectComposer.js"),
      import("three/addons/postprocessing/RenderPass.js"),
      import("three/addons/postprocessing/UnrealBloomPass.js"),
      import("three/addons/postprocessing/ShaderPass.js"),
    ]);

    // ---------- shared GLSL: classic simplex 3D noise (Ashima Arts, MIT) ----------
    const NOISE_GLSL = `
vec3 mod289(vec3 x){return x - floor(x*(1.0/289.0))*289.0;}
vec4 mod289(vec4 x){return x - floor(x*(1.0/289.0))*289.0;}
vec4 permute(vec4 x){return mod289(((x*34.0)+1.0)*x);}
vec4 taylorInvSqrt(vec4 r){return 1.79284291400159 - 0.85373472095314 * r;}
float snoise(vec3 v){
  const vec2 C = vec2(1.0/6.0, 1.0/3.0);
  const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
  vec3 i  = floor(v + dot(v, C.yyy));
  vec3 x0 = v - i + dot(i, C.xxx);
  vec3 g = step(x0.yzx, x0.xyz);
  vec3 l = 1.0 - g;
  vec3 i1 = min(g.xyz, l.zxy);
  vec3 i2 = max(g.xyz, l.zxy);
  vec3 x1 = x0 - i1 + C.xxx;
  vec3 x2 = x0 - i2 + C.yyy;
  vec3 x3 = x0 - D.yyy;
  i = mod289(i);
  vec4 p = permute(permute(permute(
             i.z + vec4(0.0, i1.z, i2.z, 1.0))
           + i.y + vec4(0.0, i1.y, i2.y, 1.0))
           + i.x + vec4(0.0, i1.x, i2.x, 1.0));
  float n_ = 0.142857142857;
  vec3 ns = n_ * D.wyz - D.xzx;
  vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
  vec4 x_ = floor(j * ns.z);
  vec4 y_ = floor(j - 7.0 * x_);
  vec4 x = x_ *ns.x + ns.yyyy;
  vec4 y = y_ *ns.x + ns.yyyy;
  vec4 h = 1.0 - abs(x) - abs(y);
  vec4 b0 = vec4(x.xy, y.xy);
  vec4 b1 = vec4(x.zw, y.zw);
  vec4 s0 = floor(b0)*2.0 + 1.0;
  vec4 s1 = floor(b1)*2.0 + 1.0;
  vec4 sh = -step(h, vec4(0.0));
  vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
  vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
  vec3 p0 = vec3(a0.xy,h.x);
  vec3 p1 = vec3(a0.zw,h.y);
  vec3 p2 = vec3(a1.xy,h.z);
  vec3 p3 = vec3(a1.zw,h.w);
  vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
  p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
  vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
  m = m * m;
  return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
}
`;

    // ---------- shared GLSL: layered fbm-ish noise used by both mesh and particles ----------
    const LOBES_GLSL = `
float lobes(vec3 p, float t, float uScale) {
  float n = snoise(p * uScale + t);
  n += 0.5 * snoise(p * uScale * 2.1 - t * 0.7 + 4.0);
  n += 0.25 * snoise(p * uScale * 4.3 + t * 1.3 + 9.0);
  return n / 1.75;
}
float surfaceDisp(vec3 p, float t, float uScale, float uAmp) {
  float n = lobes(p, t, uScale);
  float big = snoise(p * 0.8 + t * 0.15) * 0.5;
  return (n * 0.65 + big) * uAmp;
}
`;

    // ---------- shared GLSL: RGB<->HSV for continuous hue drift (public-domain utility) ----------
    const HSV_GLSL = `
vec3 rgb2hsv(vec3 c) {
  vec4 K = vec4(0.0, -1.0/3.0, 2.0/3.0, -1.0);
  vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
  vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));
  float d = q.x - min(q.w, q.y);
  float e = 1.0e-10;
  return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}
vec3 hsv2rgb(vec3 c) {
  vec4 K = vec4(1.0, 2.0/3.0, 1.0/3.0, 3.0);
  vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
  return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}
`;

    // ---------- shared GLSL: traveling waves ----------
    const WAVE_GLSL = `
float stokes(float phase) {
  return cos(phase) + 0.16 * cos(2.0 * phase);
}
float waveDisp(vec3 p, float t) {
  float w1 = stokes(p.x * 4.2 - t * 0.85);
  float w2 = stokes(p.y * 4.2 - t * 0.75 + 1.3);
  float w3 = stokes((p.x + p.y) * 2.8 + t * 1.0 + 3.0);
  float w4 = stokes((p.x - p.y) * 2.6 - t * 0.9 + 5.0);
  return w1 * 0.32 + w2 * 0.32 + w3 * 0.21 + w4 * 0.19;
}
float totalDisp(vec3 p, float t, float uScale, float uAmp, float uWaveAmp) {
  float d = surfaceDisp(p, t, uScale, uAmp);
  d += waveDisp(p, t) * uWaveAmp;
  return d;
}
`;

    const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
    renderer.setSize(window.innerWidth, window.innerHeight, false);
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.25;
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    document.body.insertBefore(renderer.domElement, document.body.firstChild);

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x030203);
    scene.fog = new THREE.FogExp2(0x030203, 0.05);

    const camera = new THREE.PerspectiveCamera(42, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 0.3, 6.5);

    const boxGroup = new THREE.Group();
    scene.add(boxGroup);

    const key = new THREE.DirectionalLight(0xdcdce8, 1.6);
    key.position.set(2.5, 4, 4);
    scene.add(key);
    scene.add(new THREE.AmbientLight(0x241f2c, 0.85));

    const sickLight = new THREE.PointLight(0x8cff4a, 0.9, 9, 2);
    sickLight.position.set(-0.6, 0.4, 0.3);
    scene.add(sickLight);
    const sickLight2 = new THREE.PointLight(0xff2d8f, 0.7, 9, 2);
    sickLight2.position.set(0.7, -0.5, 0.4);
    scene.add(sickLight2);

    const sharedUniforms = {
      uTime: { value: 0 },
      uPulseFreq: { value: 0.28 },
      uAmp: { value: 0.4 },
      uScale: { value: 1.5 },
      uWaveAmp: { value: 0.72 },
      uHueShift: { value: 0 },
      uSatShift: { value: 0 },
      uValShift: { value: 0 },
      uWallHalf: { value: 2.15 },
    };

    const geo = new THREE.PlaneGeometry(1, 1, 2, 2);
    const mesh = new THREE.Mesh(
      geo,
      new THREE.ShaderMaterial({
        uniforms: {
          ...sharedUniforms,
          uColorA: { value: new THREE.Color(0x6d17a8) },
          uColorB: { value: new THREE.Color(0x9dff4f) },
          uColorC: { value: new THREE.Color(0xff2d9e) },
          uColorD: { value: new THREE.Color(0x3d0a52) },
          uFresnelColor: { value: new THREE.Color(0x8affe0) },
          uLightPos: { value: new THREE.Vector3(48, 5, 6) },
        },
        vertexShader: `
      ${NOISE_GLSL}
      ${LOBES_GLSL}
      ${WAVE_GLSL}
      uniform float uTime;
      uniform float uPulseFreq;
      uniform float uAmp;
      uniform float uScale;
      uniform float uWaveAmp;
      uniform float uWallHalf;
      varying vec3 vNormal;
      varying vec3 vWorldPos;
      varying float vNoise;
      varying float vNoise2;
      varying float vWave;
      varying float vFoam;

      void main() {
        vec2 uv = position.xy / uWallHalf;
        vec3 p = vec3(uv, 0.0);
        float t = uTime * uPulseFreq;
        float n = lobes(p, t, uScale);
        float disp = totalDisp(p, t, uScale, uAmp, uWaveAmp);
        vec3 displaced = vec3(position.xy, disp);

        float e = 0.01;
        float du = totalDisp(vec3(uv.x + e, uv.y, 0.0), t, uScale, uAmp, uWaveAmp);
        float dv = totalDisp(vec3(uv.x, uv.y + e, 0.0), t, uScale, uAmp, uWaveAmp);
        float eWorld = e * uWallHalf;
        vec3 bumpedNormal = normalize(vec3(-(du - disp) / eWorld, -(dv - disp) / eWorld, 1.0));

        vNoise = n;
        vNoise2 = snoise(p * uScale * 1.4 - t * 0.4 + 12.0);
        vWave = waveDisp(p, t);
        vFoam = snoise(p * 9.0 + t * 2.6) * 0.5 + 0.5;
        vec4 worldPos = modelMatrix * vec4(displaced, 1.0);
        vWorldPos = worldPos.xyz;
        vNormal = normalize(mat3(modelMatrix) * bumpedNormal);
        gl_Position = projectionMatrix * viewMatrix * worldPos;
      }
    `,
        fragmentShader: `
      ${HSV_GLSL}
      uniform vec3 uColorA;
      uniform vec3 uColorB;
      uniform vec3 uColorC;
      uniform vec3 uColorD;
      uniform vec3 uFresnelColor;
      uniform vec3 uLightPos;
      uniform float uHueShift;
      uniform float uSatShift;
      uniform float uValShift;
      varying vec3 vNormal;
      varying vec3 vWorldPos;
      varying float vNoise;
      varying float vNoise2;
      varying float vWave;
      varying float vFoam;
      void main() {
        float t1 = smoothstep(-0.3, 0.75, vNoise);
        float t2 = smoothstep(0.15, 0.85, vNoise2);
        vec3 base = mix(uColorD, uColorA, t1 * 0.85 + 0.15);
        base = mix(base, uColorC, pow(t2, 2.5) * 0.55);
        base = mix(base, uColorB, pow(max(vNoise2 - 0.4, 0.0), 2.0) * 1.3);

        float crest = smoothstep(0.1, 1.0, vWave);
        vec3 waveColor = mix(uColorC, uFresnelColor, 0.4);
        base = mix(base, waveColor, crest * 0.7);
        float trough = smoothstep(-0.85, -0.15, -vWave);
        base = mix(base, uColorA * 0.55, trough * 0.45);

        float foamMask = smoothstep(0.55, 0.95, vWave) * mix(0.55, 1.0, vFoam);
        vec3 foamColor = vec3(0.92, 0.97, 1.0);

        vec3 viewDir = normalize(cameraPosition - vWorldPos);
        vec3 n = normalize(vNormal);
        float fresnel = pow(1.0 - max(dot(n, viewDir), 0.0), 2.2);

        vec3 lightDir = normalize(uLightPos - vWorldPos);
        vec3 halfDir = normalize(lightDir + viewDir);
        float spec = pow(max(dot(n, halfDir), 0.0), 55.0);
        float spec2 = pow(max(dot(n, halfDir), 0.0), 16.0) * 0.18;

        vec3 fillDir = normalize(vec3(0.0, 0.35, 1.0));
        float fillDiff = max(dot(n, fillDir), 0.0);
        float wrap = max(dot(n, fillDir) * 0.5 + 0.5, 0.0);

        base = mix(base, foamColor, foamMask);
        vec3 color = base * (0.6 + fillDiff * 0.52 + wrap * 0.28) + uFresnelColor * fresnel * 0.6;
        color += vec3(1.0, 0.98, 0.92) * (spec * 1.4 + spec2);

        vec3 hsv = rgb2hsv(color);
        hsv.x = fract(hsv.x + uHueShift);
        hsv.y = clamp(hsv.y * (1.6 + uSatShift), 0.0, 1.0);
        hsv.z = clamp(hsv.z * (1.0 + uValShift), 0.0, 1.4);
        color = hsv2rgb(hsv);

        gl_FragColor = vec4(color, 1.0);
      }
    `,
      })
    );
    mesh.position.z = -0.6;
    boxGroup.add(mesh);

    const WALL_OVERSCAN = 1.3;
    function fitWallToView() {
      const dist = camera.position.z - mesh.position.z;
      const vFovRad = THREE.MathUtils.degToRad(camera.fov);
      const halfH = Math.tan(vFovRad / 2) * dist * WALL_OVERSCAN;
      const halfW = halfH * camera.aspect;
      sharedUniforms.uWallHalf.value = halfH;
      const segY = 170;
      const segX = Math.min(260, Math.round(segY * Math.max(camera.aspect, 1)));
      mesh.geometry.dispose();
      mesh.geometry = new THREE.PlaneGeometry(halfW * 2, halfH * 2, segX, segY);
    }
    fitWallToView();

    const composer = new EffectComposer(renderer);
    composer.addPass(new RenderPass(scene, camera));
    const bloomPass = new UnrealBloomPass(
      new THREE.Vector2(window.innerWidth, window.innerHeight),
      0.45,
      0.4,
      0.82
    );
    composer.addPass(bloomPass);

    const tripPass = new ShaderPass({
      uniforms: {
        tDiffuse: { value: null },
        uTime: { value: 0 },
        uAberration: { value: 0.0028 },
        uGrain: { value: 0.06 },
        uVignette: { value: 0.12 },
      },
      vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
      fragmentShader: `
    uniform sampler2D tDiffuse;
    uniform float uTime;
    uniform float uAberration;
    uniform float uGrain;
    uniform float uVignette;
    varying vec2 vUv;
    void main() {
      vec2 dir = vUv - 0.5;
      float dist = length(dir);
      vec2 offset = dir * uAberration * (0.4 + dist);
      float r = texture2D(tDiffuse, vUv - offset).r;
      float g = texture2D(tDiffuse, vUv).g;
      float b = texture2D(tDiffuse, vUv + offset).b;
      vec3 color = vec3(r, g, b);
      float grain = (fract(sin(dot(vUv * (uTime * 60.0 + 1.0), vec2(12.9898, 78.233))) * 43758.5453) - 0.5) * uGrain;
      color += grain;
      float vig = 1.0 - smoothstep(0.15, 1.0, dist * (1.0 + uVignette));
      color *= mix(0.6, 1.0, vig);
      gl_FragColor = vec4(color, 1.0);
    }
  `,
    });
    tripPass.renderToScreen = true;
    composer.addPass(tripPass);

    const clock = new THREE.Clock();
    // re-rolled on every page load so the color drift below starts at a different point in
    // its cycle each time, instead of always opening on the same mix
    const colorPhaseOffset = Math.random() * 1000;
    const baseAmp = sharedUniforms.uAmp.value;
    const basePulse = sharedUniforms.uPulseFreq.value;
    const baseWaveAmp = sharedUniforms.uWaveAmp.value;
    function pulseShape(phase) {
      const s = Math.sin(phase * Math.PI * 2.0);
      return Math.sign(s) * Math.pow(Math.abs(s), 0.4);
    }
    let lastFlinchStart = -Infinity;
    let nextFlinch = 4 + Math.random() * 5;
    const drawFrame = () => {
      const t = clock.getElapsedTime();
      const escalation = Math.min(t / 45, 1);
      const heartbeatFreq = 0.55 + escalation * 1.5;

      if (t >= nextFlinch) {
        lastFlinchStart = t;
        nextFlinch = t + 5 + Math.random() * 9;
      }
      const flinch = Math.exp(-Math.max(0, t - lastFlinchStart) * 7.0) * (t >= lastFlinchStart ? 1 : 0);

      sharedUniforms.uTime.value = t;
      sharedUniforms.uPulseFreq.value = basePulse + escalation * 0.35;
      const beat = pulseShape(t * heartbeatFreq);
      sharedUniforms.uAmp.value = baseAmp * (1.0 + 0.22 * beat + flinch * 0.5);
      sharedUniforms.uWaveAmp.value = baseWaveAmp * (1.0 + 0.3 * Math.max(beat, 0.0) + flinch * 0.5);

      const throb = 0.5 + 0.5 * beat;
      sickLight.intensity = 0.6 + throb * 0.7 + escalation * 0.3 + flinch * 1.2;
      sickLight2.intensity = 0.4 + (1 - throb) * 0.6 + escalation * 0.25 + flinch * 0.9;

      const shudder = Math.max(beat - 0.7, 0.0) * 0.06 + flinch * 0.09;
      camera.position.x = Math.sin(t * 0.045) * 0.4 + Math.sin(t * 47.0) * shudder;
      camera.position.y = 0.3 + Math.cos(t * 0.037) * 0.22 + Math.cos(t * 53.0) * shudder;
      camera.position.z = 6.5 + Math.sin(t * 0.021) * 0.15;
      camera.lookAt(0, 0.3, 0.2);

      tripPass.uniforms.uTime.value = t;
      tripPass.uniforms.uAberration.value = 0.0022 + escalation * 0.0022 + throb * 0.0008 + flinch * 0.006;

      const tc = t + colorPhaseOffset;
      sharedUniforms.uHueShift.value =
        0.26 * Math.sin(tc * 0.09) +
        0.14 * Math.sin(tc * 0.033 + 2.0) +
        0.08 * Math.sin(tc * 0.21 + 5.0) +
        flinch * 0.4;
      sharedUniforms.uSatShift.value =
        0.28 * Math.sin(tc * 0.05 + 1.0) + 0.15 * Math.sin(tc * 0.13 + 4.0) + flinch * 0.3;
      sharedUniforms.uValShift.value = 0.12 * Math.sin(tc * 0.037 + 2.5) + flinch * 0.2;

      composer.render();
    };
    window.addEventListener("resize", () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight, false);
      composer.setSize(window.innerWidth, window.innerHeight);
      bloomPass.setSize(window.innerWidth, window.innerHeight);
      fitWallToView();
    });
  
    drawFrame();
    clock.stop();
    let pausedElapsed = clock.elapsedTime;
    let isRunning = false;
    const pause = () => {
      if (!isRunning) return;
      renderer.setAnimationLoop(null);
      clock.stop();
      pausedElapsed = clock.elapsedTime;
      isRunning = false;
    };
    const resume = () => {
      if (isRunning) return;
      clock.start();
      clock.elapsedTime = pausedElapsed;
      isRunning = true;
      renderer.setAnimationLoop(drawFrame);
    };
    window.addEventListener('resize', () => { if (!isRunning) drawFrame(); });
    window.addEventListener('pagehide', () => {
      pause();
      composer.dispose();
      mesh.geometry.dispose();
      mesh.material.dispose();
      renderer.dispose();
    });
    return { pause, resume };

}
