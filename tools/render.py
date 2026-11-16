from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = json.loads((ROOT / 'assets/art/dimensions.json').read_text())

COLLECTIONS = [
    {
        'slug': 'processing-studies', 'title': 'Processing Studies', 'number': 'CF—GA—001',
        'category': 'generative', 'year': 'Year to confirm', 'medium': 'Generative art / Processing',
        'lead': 'Fragments accumulate. An image takes shape.',
        'description': 'Four still outputs made with Processing scripts by Roger Link. Bright color, patterned fragments, muted photographic textures, and a restrained ochre field offer four different densities of the same fragmented visual language. These are saved images, not a live browser animation. Collection and image captions are descriptive working labels.',
        'source': 'https://github.com/roger-link/processing',
        'images': [('processing-color', 'Color fragments', 'Overlapping angular fragments in pink, violet, blue, red, and orange form a dense image.'), ('processing-pattern', 'Pattern fragments', 'Black-and-white patterned fragments are interspersed with sharp yellow, blue, and magenta shapes.'), ('processing-earth', 'Muted fragments', 'Layered angular fragments of muted brown, gray, green, and cream photographic textures.'), ('processing-ochre', 'Ochre field', 'A dense field of translucent ochre and olive angular shapes against dark gaps.')],
    },
    {
        'slug': 'bicycle-2007', 'title': 'Bicycle, 2007', 'number': 'CF—PH—001',
        'date': 'April 23, 2007',
        'category': 'photography', 'year': '2007', 'medium': 'Color-inverted photographs',
        'lead': 'A familiar body. An unfamiliar surface.',
        'description': 'A few moments with a bicycle, turned inside out by inverted color.',
        'images': [('bicycle-arms', 'Tattooed arm and gloves', 'A cropped tattooed arm turned cyan beside a bicycle and pale work gloves.'), ('bicycle-legs', 'Legs / wheel', 'Cropped legs, a bicycle wheel, and a pedal against a grid of pavement.'), ('bicycle-alley', 'Seated, in the alley', 'A seated person beside a blue bicycle in a color-inverted brick alley.'), ('bicycle-overhead', 'Bicycle overhead', 'A figure holding a pale bicycle overhead against a brick wall.')],
    },
    {
        'slug': 'body-exposure', 'title': 'Body / Exposure', 'number': 'CF—PH—002',
        'category': 'photography', 'year': '2009', 'medium': 'Photographs',
        'lead': 'Presence, interruption, disappearance.',
        'description': 'Moving bodies and still rooms, recorded at different speeds. A figure gathers and disperses; a seated observer remains. Four photographs arranged as a sequence rather than a collection of blur effects.',
        'images': [('body-pink', 'Pink room', 'A dark moving figure in a pink-lit room.'), ('body-arms', 'Extended arms', 'An indistinct blue-lit figure with extended arms.'), ('body-observer', 'Figure and observer', 'A large blue apparition above a small seated person in the same room.'), ('body-hallway', 'Hallway', 'Overlapping dark figures disperse through a dim hallway toward a patch of light.')],
    },
    {
        'slug': 'sixteen', 'title': 'Sixteen', 'number': 'CF—PH—003',
        'category': 'photography', 'year': '2008', 'medium': 'Photographs',
        'lead': 'Small geometries of an ordinary interior.',
        'description': 'Two selected photographs from an interior sequence: the seams of a dark tiled corner and a narrow line of trim against a teal wall. Light and framing make the everyday surface almost abstract.',
        'images': [('sixteen-tiles', 'Tiled corner', 'Thin greenish seams meet across a nearly black tiled corner.'), ('sixteen-trim', 'Wall / trim', 'A nearly empty teal wall above a narrow golden line of trim and a dark floor.')],
    },
    {
        'slug': 'drawn-fields', 'title': 'Drawn Fields', 'number': 'CF—DR—001',
        'category': 'drawing', 'year': '2025', 'medium': 'Digital drawings',
        'lead': 'Lines accumulate. Shapes drift out of alignment.',
        'description': 'Eight drawings moving between open networks on dark grounds, dense ribbon-like gestures, pale fields of suspended fragments, and sharply colored forms. The sequence shifts between fine line, layered color, and broad gestures. Captions are descriptive labels rather than formal artwork titles.',
        'images': [('drawing-network', 'Open network', 'Fine multicolored lines and pale organic fragments suspended on a black ground.'), ('drawing-ribbons', 'Ribbons', 'Dense loops of pink, blue, green, and yellow marks interweave across the image.'), ('drawing-pale', 'Pale field', 'Transparent pastel fragments, fine meshes, and darker interruptions in a pale atmospheric field.'), ('drawing-purple', 'Orange / purple', 'Angular orange and turquoise shapes float in a purple field crossed by finer lines.'), ('drawing-electric', 'Electric forms', 'Vivid orange, blue, and green shapes overlap black and pale yellow ribbons on a grainy gray ground.'), ('drawing-blue-pink', 'Blue / pink', 'Looping multicolored outlines cross layered pale pink, lime, teal, and deep blue fields.'), ('drawing-teal-violet', 'Teal / violet', 'Broad teal, orange, and violet gestures intersect with fine pink, yellow, and white lines.'), ('drawing-peach', 'Peach field', 'Blue strokes and pale folded forms float among dark shapes and fluorescent marks on a peach ground.')],
    },
    {
        'slug': 'facades-grids', 'title': 'Facades / Grids', 'number': 'CF—DS—001',
        'category': 'spatial', 'year': '2022', 'medium': 'Digital image studies',
        'lead': 'A system, interrupted.',
        'description': 'Stripes, windows, and repeated divisions become color structures. A small dark box, a doorway, or an uneven grid interrupts the apparent order. Three selected image studies.',
        'images': [('facade-stripes', 'Stripes / dark box', 'A small dark box interrupts dense vertical green, white, blue, and red stripes.'), ('facade-yellow', 'Yellow facade', 'A pale yellow building with a blue central door beneath a flat pink sky.'), ('facade-grid', 'Window grid', 'A blue and green facade divided by an irregular pale window grid.')],
    },
    {
        'slug': 'rooms-without-occupants', 'title': 'Rooms Without Occupants', 'number': 'CF—DS—002',
        'category': 'spatial', 'year': '2022', 'medium': 'Digital image studies',
        'lead': 'Openings without a clear destination.',
        'description': 'Two empty spaces organized by colored walls, apertures, and displaced planes of light. The absence of occupants leaves the geometry unresolved.',
        'images': [('room-purple', 'Purple room', 'A purple room with ochre doorways and an apparently displaced rectangular plane of light.'), ('room-green', 'Green opening', 'A green rectangular opening in a pale room bordered by pink walls.')],
    },
    {
        'slug': 'works-on-paper', 'title': 'Works on Paper', 'number': 'CF—WP—001',
        'category': 'paper', 'year': '2025', 'medium': 'Drawings and works on paper',
        'lead': 'A surface that remembers its earlier marks.',
        'description': 'Five works on paper, moving from a warm layered surface through open yellow passages, looping colored lines, and white gestures to a dense dark network. Paper texture and overlapping marks remain visible. Captions are descriptive labels rather than formal artwork titles.',
        'images': [('paper-warm', 'Layered sheet', 'A warm orange and red layered abstraction on paper, with dark loops and partly buried colored marks.'), ('paper-yellow-lines', 'Yellow / wandering lines', 'Dark burgundy lines wander across a pale yellow field with faint green, gray, and white marks on textured paper.'), ('paper-color-loops', 'Colored loops', 'Red, green, blue, ochre, and rose strokes loop across a pale paper ground, interspersed with fine gray lines.'), ('paper-white-gestures', 'White gestures', 'White gestural marks interrupt layered pink, orange, green, and blue forms and fine dark outlines on paper.'), ('paper-dark-network', 'Dark network', 'Dense black looping strokes cross red, magenta, and teal marks, leaving small openings of pale paper.')],
    },
]


def image(slug, alt, prefix, lazy=True, sizes='(max-width: 600px) 92vw, 48vw'):
    loading = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    variants = {}
    for rendition in (480, 960, 1600):
        width = DIMENSIONS[f'{slug}-{rendition}']['width']
        variants[width] = f'{prefix}assets/art/{slug}-{rendition}.webp {width}w'
    srcset = ', '.join(variants.values())
    dimensions = DIMENSIONS[f'{slug}-960']
    return f'<img src="{prefix}assets/art/{slug}-960.webp" srcset="{srcset}" sizes="{sizes}" width="{dimensions["width"]}" height="{dimensions["height"]}" alt="{escape(alt, quote=True)}" decoding="async"{loading}>'


def nav(prefix, current=''):
    items = [('Works', 'works/'), ('Recordings', 'recordings/'), ('Instruments', 'unfold/'), ('Experiments', 'experiments/'), ('About', 'about/')]
    return '<nav class="nav" aria-label="Main navigation">' + ''.join(f'<a href="{prefix}{path}"' + (' aria-current="page"' if name == current else '') + f'>{name}</a>' for name, path in items) + '</nav>'


def footer(prefix):
    return f'<footer class="footer wrap"><a href="{prefix}">Cancelled Futures © 2026</a><span>All items subject to change</span><a href="https://cancelledfutures.bandcamp.com/">Bandcamp ↗</a></footer>'


def document(title, description, content, prefix='./', current='', home=False, extra_script=''):
    header = '' if home else f'<header class="compact-header wrap"><a class="wordmark" href="{prefix}" aria-label="Cancelled Futures home">CANCELLED FUTURES<span>.</span></a>{nav(prefix, current)}</header>'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f0eadf">
  <title>{escape(title)} — Cancelled Futures</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:title" content="{escape(title, quote=True)} — Cancelled Futures">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <link rel="icon" href="{prefix}assets/editorial-mark.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}assets/editorial.css">
  <script src="{prefix}assets/archive.js" defer></script>
  {extra_script}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  {header}
  <main id="main">{content}</main>
  {footer(prefix)}
</body>
</html>
'''


def write(path, content):
    destination = ROOT / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text('\n'.join(line.rstrip() for line in content.splitlines()) + '\n', encoding='utf-8')


def heading(kicker, title, lead, note=''):
    return f'<section class="page-heading wrap"><p class="kicker">{kicker}</p><h1>{title}</h1><p class="lead serif">{lead}</p>' + (f'<p class="page-note">{note}</p>' if note else '') + '</section>'


def album_art(prefix):
    if (ROOT / 'assets/art/plastic-memory-960.webp').exists():
        return image('plastic-memory', 'Original Plastic Memory cover: irregular pink, green, orange, and yellow forms over a dark layered surface.', prefix, lazy=False)
    return '<div class="empty-art">Original album artwork to be added</div>'


def home():
    rows = [
        ('01', 'Plastic Memory', 'Recording / Forthcoming', 'recordings/plastic-memory/'),
        ('02', 'Unfold', 'Instrument / In development', 'unfold/'),
        ('03', 'Photography', 'Selected series / 2007–2009', 'works/?category=photography'),
        ('04', 'Drawn Fields', 'Drawings / 2025', 'works/drawn-fields/'),
        ('05', 'Spatial Studies', 'Image studies / 2022', 'works/?category=spatial'),
        ('06', 'Works on Paper', 'Selected work / 2025', 'works/works-on-paper/'),
        ('07', 'Wave Sculpture', 'Moving image / Live JavaScript', 'experiments/wave-sculpture/'),
        ('08', 'Whoop Dee Doo', 'Collaborative installations', 'whoop-dee-doo/'),
        ('09', 'Processing Studies', 'Generative art / Selected stills', 'works/processing-studies/'),
    ]
    index = ''.join(f'<a class="index-row" href="{url}"><span class="index-number">{number}</span><span class="index-title">{title}</span><span class="index-detail">{detail}</span><span class="index-arrow" aria-hidden="true">↗</span></a>' for number, title, detail, url in rows)
    content = f'''<div class="wrap">
      <header><div class="topline mono"><span>CF / An independent operation</span><span>Recordings · Instruments · Experiments</span></div>
      <div class="masthead"><h1><span>CANCELLED</span><span>FUTURES<span class="period">.</span></span></h1><p class="tagline serif">Music and other accidents.</p></div>{nav('./', 'Works')}</header>
      <section class="feature" aria-labelledby="featured-title"><figure class="feature-art"><a href="recordings/plastic-memory/" aria-label="Explore Plastic Memory">{album_art('./')}</a><figcaption class="mono"><span>CF—REC—001</span><span>Original cover artwork</span></figcaption></figure>
      <div class="feature-copy"><p class="kicker">Current work / CF—REC—001</p><h2 id="featured-title">Plastic<br>Memory</h2><p class="deck serif">Electronic recordings.<br>Patterns, fragments, and things left open.</p><p class="description">A forthcoming album by Cancelled Futures.</p><a class="editorial-link" href="recordings/plastic-memory/">Explore the recording <span aria-hidden="true">↗</span></a><p class="release mono"><span class="status-line">Forthcoming · Listening details to follow</span></p></div></section>
      <section class="index-section" id="index" aria-labelledby="index-title"><div class="section-head"><h2 id="index-title">The Index</h2><p class="serif">A growing collection of recordings, instruments, and experiments.</p></div><div class="index-list">{index}</div><a class="editorial-link" href="works/" style="margin-top:22px">Browse the visual archive <span aria-hidden="true">↗</span></a></section>
      <section class="about-strip" aria-labelledby="about-title"><div><p class="kicker">About</p><h2 class="statement serif" id="about-title">An ongoing collection of recordings, instruments, and experiments.</h2><p class="byline">An independent practice by Roger Link.</p><a class="editorial-link" href="about/">About the project <span aria-hidden="true">↗</span></a></div><div class="cf-stamp" aria-hidden="true"><strong>CF.</strong><span>CANCELLED<br>FUTURES<br>—</span></div></section>
    </div>'''
    write('index.html', document('Music and other accidents', 'Recordings, instruments, photography, drawings, and experiments by Roger Link. Plastic Memory is forthcoming.', content, home=True))


def works():
    cards = []
    for collection in COLLECTIONS:
        slug, title, alt = collection['images'][0]
        count = len(collection['images'])
        cards.append(f'''<article class="work-card" data-category="{collection['category']}"><a href="{collection['slug']}/"><div class="cover">{image(slug, alt, '../', sizes='(max-width: 600px) 44vw, (max-width: 900px) 46vw, 30vw')}</div><p class="meta"><span>{collection['number']}</span><span>{collection['year']} / {count} {'work' if count == 1 else 'works'}</span></p><h2>{collection['title']} <span aria-hidden="true">↗</span></h2></a><p class="card-note">{collection['medium']}</p></article>''')
    cards.append(f'<article class="work-card" data-category="moving"><a href="../experiments/wave-sculpture/"><div class="cover">{image("wave-warm", "Still frame from the warm version of Wave Sculpture, a moving field of carved forms and colored light.", "../")}</div><p class="meta"><span>CF—GV—001</span><span>Two versions / Live work</span></p><h2>Wave Sculpture <span aria-hidden="true">↗</span></h2></a><p class="card-note">Generative moving image / JavaScript</p></article>')
    cards.append(f'<article class="work-card" data-category="collaborative"><a href="../whoop-dee-doo/"><div class="cover">{image("tba-room", "Whoop Dee Doo installation for TBA: a reflective purple-lit room with a sculptural brain and projected image.", "../")}</div><p class="meta"><span>Whoop Dee Doo</span><span>TBA / Portland</span></p><h2>Whoop Dee Doo <span aria-hidden="true">↗</span></h2></a><p class="card-note">Collaborative installations / Project documentation</p></article>')
    filters = [('all', 'All works'), ('photography', 'Photography'), ('drawing', 'Drawings'), ('spatial', 'Spatial studies'), ('paper', 'On paper'), ('generative', 'Generative art'), ('moving', 'Moving image'), ('collaborative', 'Collaborative')]
    buttons = ''.join(f'<button class="filter" type="button" data-filter="{key}" aria-pressed="{str(key == "all").lower()}">{label}</button>' for key, label in filters)
    content = heading('CF / Visual archive', 'Selected works<span style="color:var(--rust)">.</span>', 'Photography, drawings, surfaces, and uncertain spaces.', 'An edited archive, organized as collections. Open a series to follow its sequence.')
    content += f'<div class="wrap"><div class="filters" role="group" aria-label="Filter collections">{buttons}</div><p class="visually-hidden" id="filter-status" role="status" aria-live="polite"></p><div class="work-grid">{"".join(cards)}</div></div>'
    write('works/index.html', document('Selected works', 'An edited visual archive of photography, drawings, works on paper, and spatial image studies.', content, '../', 'Works'))


def series():
    for index, collection in enumerate(COLLECTIONS):
        figures = []
        for position, (slug, title, alt) in enumerate(collection['images'], start=1):
            caption = escape(title, quote=True)
            figures.append(f'<figure><a class="image-link" href="../../assets/art/{slug}-1600.webp" data-view-image data-caption="{caption}" aria-label="Enlarge: {caption}">{image(slug, alt, "../../", lazy=position != 1, sizes="(max-width: 600px) 92vw, 80vw" if position == 1 else "(max-width: 600px) 92vw, 45vw")}</a><figcaption><span>{title}</span><span>{position:02d} / {len(collection["images"]):02d}</span></figcaption></figure>')
        content = heading(collection['number'] + ' / ' + collection.get('date', collection['year']), collection['title'], collection['lead'])
        if collection.get('source'):
            content += f'<div class="wrap"><a class="editorial-link" href="{escape(collection["source"], quote=True)}" style="margin-top:24px">View the Processing scripts <span aria-hidden="true">↗</span></a></div>'
        content += f'<div class="wrap"><div class="series-intro"><p>{collection["description"]}</p><dl class="series-meta"><div><dt>Collection</dt><dd>{collection["medium"]}</dd></div><div><dt>Selection</dt><dd>{len(figures)} works</dd></div><div><dt>Artist</dt><dd>Roger Link</dd></div><div><dt>Archive</dt><dd><a href="../">All collections ↗</a></dd></div></dl></div><div class="gallery">{"".join(figures)}</div>'
        previous = COLLECTIONS[(index - 1) % len(COLLECTIONS)]
        following = COLLECTIONS[(index + 1) % len(COLLECTIONS)]
        content += f'<nav class="series-pagination" aria-label="Browse collections"><a href="../{previous["slug"]}/"><small>Previous collection</small>← {previous["title"]}</a><a href="../{following["slug"]}/"><small>Next collection</small>{following["title"]} →</a></nav></div>'
        content += '''<dialog class="viewer" id="viewer" aria-label="Artwork viewer"><div class="viewer-layout"><div class="viewer-top"><span data-view-position aria-live="polite"></span><button type="button" data-view-close autofocus>Close ×</button></div><figure><img src="" alt=""></figure><div class="viewer-bottom"><span data-view-caption></span><div class="viewer-controls"><button type="button" data-view-previous aria-label="Previous image">← Previous</button><button type="button" data-view-next aria-label="Next image">Next →</button></div></div></div></dialog>'''
        write(f'works/{collection["slug"]}/index.html', document(collection['title'], collection['description'], content, '../../', 'Works'))


def recordings():
    content = heading('CF / Recordings', 'Recordings<span style="color:var(--rust)">.</span>', 'Music and other accidents.')
    content += f'<div class="wrap"><section class="record-page"><a href="plastic-memory/" aria-label="Explore Plastic Memory">{album_art("../")}</a><div><p class="kicker">CF—REC—001 / Forthcoming</p><h2 class="record-title">Plastic Memory</h2><p class="lead serif">Electronic recordings.<br>Patterns, fragments, and things left open.</p><p>A forthcoming album by Cancelled Futures. Listening details will be added when the album is available.</p><a class="editorial-link" href="plastic-memory/">Recording notes <span aria-hidden="true">↗</span></a></div></section></div>'
    write('recordings/index.html', document('Recordings', 'Plastic Memory, a forthcoming album by Cancelled Futures.', content, '../', 'Recordings'))
    content = f'<div class="wrap"><section class="record-page"><figure>{album_art("../../")}<figcaption class="meta" style="margin-top:12px">Plastic Memory / Original cover artwork</figcaption></figure><div><p class="kicker">Current work / CF—REC—001</p><h1>Plastic<br>Memory</h1><p class="lead serif">Music and other accidents.</p><p>Electronic recordings by Cancelled Futures.</p><p><span class="status-line mono">Forthcoming</span></p><p>Listening details, release information, and album notes will be added here when the recording is ready to share.</p><a class="editorial-link" href="../../works/">Explore the visual archive <span aria-hidden="true">↗</span></a><p class="meta" style="margin-top:28px">No release date announced.</p></div></section><nav class="series-pagination" aria-label="Related work"><a href="../">← All recordings</a><a href="../../unfold/">Unfold →</a></nav></div>'
    write('recordings/plastic-memory/index.html', document('Plastic Memory', 'Plastic Memory, forthcoming electronic recordings by Cancelled Futures. Listening details to follow.', content, '../../', 'Recordings'))


def about():
    content = heading('CF / An independent operation', 'About<span style="color:var(--rust)">.</span>', 'An ongoing collection of recordings, instruments, and experiments.')
    content += '<div class="wrap"><div class="prose"><p>Cancelled Futures is where I bring together the things I make: electronic music, photographs, drawings, generative art, and tools for making more.</p><p>Some start with a sound, others with a mark or a bit of code. This archive gives them a place to sit alongside one another, without needing them all to fit the same mold.</p><h2>Two ways in.</h2><p>Start with <a class="editorial-link" href="../recordings/">the recordings ↗</a>, or follow a sequence through <a class="editorial-link" href="../works/">the visual archive ↗</a>.</p><p>Unfold is a generative music studio for Mac, currently in development. It offers another way into the practice: an instrument for exploring musical possibilities.</p><a class="editorial-link" href="https://rogerlink.com/">More about Roger Link <span aria-hidden="true">↗</span></a></div></div>'
    portrait = f'<figure class="about-portrait">{image("about-jaimie-warren", "Close-up portrait with a gray wig and pink and white face paint, holding a burger.", "../", lazy=False, sizes="(max-width: 600px) 92vw, 40vw")}<figcaption>Photograph by Jaimie Warren</figcaption></figure>'
    content = content.replace('<div class="wrap"><div class="prose">', f'<div class="wrap about-layout">{portrait}<div class="prose">', 1)
    write('about/index.html', document('About', 'Cancelled Futures is an independent creative practice by Roger Link: recordings, instruments, and visual experiments.', content, '../', 'About'))


def unfold():
    rows = ''.join(f'<div class="phrase-row"><span class="phrase-name">{label}</span><div class="note-grid" data-row="{index}"></div></div>' for index, label in enumerate(('01 / Begin', '02 / Follow', '03 / Respond')))
    content = heading('CF / Instruments / In development', 'Unfold<span style="color:var(--rust)">.</span>', 'An instrument for surprising yourself.')
    content += f'<div class="wrap"><section class="instrument-grid"><div><div class="instrument-art" role="img" aria-label="Visual phrase illustration, not the app interface. No audio.">{rows}</div><div class="pattern-caption"><span>Phrase illustration / No audio</span><button type="button" id="new-pattern">Another possibility ↻</button></div><p class="visually-hidden" id="pattern-status" role="status" aria-live="polite"></p><noscript><p class="meta">Enable JavaScript to explore the visual phrase illustration.</p></noscript></div><div class="instrument-copy"><p class="kicker">Generative music studio / Mac</p><h2>Start with a phrase.<br><span class="serif">See what unfolds.</span></h2><p>Build a phrase, bring in related voices, and shape the music as it plays. Keep an idea you like. Record what happens.</p><p>Explore Still, Drift, and Renew behavior. Save editable Pieces and Keep snapshots, then record a stereo take and export a WAV.</p><p class="mono"><span class="status-line">Mac release in preparation</span></p><p>Free and open source. The first public Mac download is being prepared.</p><a class="editorial-link" href="https://github.com/roger-link/unfold">Follow the project <span aria-hidden="true">↗</span></a><p class="meta" style="margin-top:20px">Planned licence: AGPL-3.0-only.<br>Music you make with it is yours.</p></div></section></div>'
    write('unfold/index.html', document('Unfold', 'A generative music studio for Mac by Cancelled Futures. Free and open source; release in preparation.', content, '../', 'Instruments', extra_script='<script src="../assets/pattern.js" defer></script>'))


def experiments():
    stylesheet = '<link rel="stylesheet" href="../assets/wave/player.css">'
    content = heading('CF / Experiments', 'Experiments<span style="color:var(--rust)">.</span>', 'Systems in motion. Outcomes left open.')
    content += f'<div class="wrap"><article class="experiment-card"><a href="wave-sculpture/" aria-label="Explore Wave Sculpture">{image("wave-warm", "Still frame from Wave Sculpture: a dimensional field of dark forms and warm light.", "../", lazy=False)}</a><div><p class="kicker">CF—GV—001 / Generative moving image</p><h2>Wave Sculpture</h2><p class="serif" style="font-size:30px;line-height:1.15">A surface that never quite settles.</p><p>Two versions of a real-time JavaScript work. Shifting color, carved depth, pulsing light, and a continuously changing surface.</p><a class="editorial-link" href="wave-sculpture/">Play the work <span aria-hidden="true">↗</span></a></div></article><div class="series-pagination"><a href="../works/?category=spatial">Spatial image studies →</a><a href="../works/">All visual work →</a></div></div>'
    processing_card = f'<article class="experiment-card"><a href="../works/processing-studies/" aria-label="Explore Processing Studies">{image("processing-color", "Dense pink, blue, and orange fragments from a generative Processing artwork.", "../")}</a><div><p class="kicker">CF—GA—001 / Generative art</p><h2>Processing Studies</h2><p class="serif" style="font-size:30px;line-height:1.15">Fragments accumulate.</p><p>Four saved outputs made with Processing scripts. Color, pattern, and image fragments gather into densely layered fields.</p><a class="editorial-link" href="../works/processing-studies/">View the stills <span aria-hidden="true">↗</span></a></div></article>'
    content = content.replace('<div class="series-pagination">', processing_card + '<div class="series-pagination">', 1)
    write('experiments/index.html', document('Experiments', 'Generative art made with Processing and real-time JavaScript moving images by Roger Link.', content, '../', 'Experiments', extra_script=stylesheet))
    content = heading('CF—GV—001 / Generative moving image', 'Wave Sculpture', 'A surface that never quite settles.', 'Contains pulsing light and camera motion. Nothing moves until you choose Play. No audio.')
    content += f'''<div class="wrap"><section class="wave-player" data-wave-player data-frame-url="../../assets/wave/frame.html" data-poster-base="../../assets/art/" aria-label="Wave Sculpture player">
      <div class="wave-stage" data-wave-stage id="wave-stage">{image('wave-warm', 'Still frame from the original Wave Sculpture. Use Play to see the live moving work.', '../../', lazy=False, sizes='92vw')}</div>
      <div class="wave-toolbar"><div class="wave-controls"><button type="button" data-wave-play aria-pressed="false" aria-controls="wave-stage">Play moving work</button><button type="button" data-wave-restart>Restart</button><button type="button" data-wave-fullscreen>Fullscreen</button></div><div class="wave-versions" role="group" aria-label="Artwork version"><button type="button" data-wave-variant="warm" aria-pressed="true">Warm relief</button><button type="button" data-wave-variant="drift" aria-pressed="false">Color drift</button></div></div>
      <p class="wave-status" data-wave-status role="status" aria-live="polite">Still frame shown. Press Play to run the original JavaScript artwork.</p><noscript><p>JavaScript and WebGL are needed to play this work. A still frame is shown above.</p></noscript>
      </section><div class="wave-notes"><p>Two versions of the work originally presented on <a class="editorial-link" href="https://rogerlink.com/">rogerlink.com ↗</a>. The warm version emphasizes relief and material depth; the other lets color drift further. These labels distinguish the versions, rather than assigning new titles to separate works.</p><p>Made by Roger Link using JavaScript, Three.js, and custom shaders. Generated live in your browser, not a recorded video. Each restart begins a fresh run. Playback pauses when the work leaves the screen or the tab is hidden.</p></div><nav class="series-pagination" aria-label="Related work"><a href="../">← All experiments</a><a href="../../works/">Visual archive →</a></nav></div>'''
    scripts = '<link rel="stylesheet" href="../../assets/wave/player.css"><script src="../../assets/wave/player.js" defer></script>'
    write('experiments/wave-sculpture/index.html', document('Wave Sculpture', 'A real-time generative moving image by Roger Link. Play two versions of the original JavaScript artwork.', content, '../../', 'Experiments', extra_script=scripts))


def whoop_dee_doo():
    content = heading('CF / Collaborative work', 'Whoop Dee Doo', 'Environments made together.', 'Selected project documentation, presented separately from the independent visual work.')
    content += f'<div class="wrap"><section class="record-page"><a href="tba/" aria-label="Explore the TBA installation">{image("tba-room", "Reflective walls, colored light, a sculptural brain, and a projection inside the TBA installation.", "../", lazy=False)}</a><div><p class="kicker">Installation / Portland</p><h2 class="record-title">TBA installation</h2><p class="lead serif">A room for the brain.</p><p>An interactive environment made through Whoop Dee Doo for the Time-Based Art Festival. Found materials, colored light, and projected memories turn a room into an imagined interior of the body.</p><a class="editorial-link" href="tba/">View the project <span aria-hidden="true">↗</span></a></div></section><nav class="series-pagination" aria-label="Related work"><a href="../works/">← Visual archive</a><a href="../about/">About the practice →</a></nav></div>'
    baltimore_card = f'<section class="record-page"><a href="baltimore/" aria-label="Explore the Baltimore show">{image("baltimore-performance", "Costumed performers in a constructed Whoop Dee Doo set with a large face above the stage.", "../")}</a><div><p class="kicker">Live show / Baltimore</p><h2 class="record-title">Baltimore show</h2><p class="lead serif">A set becomes a gathering.</p><p>Three photographs of a Whoop Dee Doo show: the performance, the audience, and the room in use.</p><a class="editorial-link" href="baltimore/">View the project <span aria-hidden="true">↗</span></a></div></section>'
    content = content.replace('<nav class="series-pagination"', baltimore_card + '<nav class="series-pagination"', 1)
    write('whoop-dee-doo/index.html', document('Whoop Dee Doo', 'Collaborative work through Whoop Dee Doo: an interactive installation for TBA in Portland and a live show in Baltimore.', content, '../', 'Works'))
    images = [
        ('tba-room', 'Room view', 'A purple and red-lit installation with reflective circular forms covering the left wall, a sculptural brain in the foreground, and a projection at the back.'),
        ('tba-wall', 'Reflective wall / detail', 'Metallic bowls and smaller reflective forms catch purple, red, and green light against dark plastic-covered walls.'),
        ('tba-projection', 'Projection / interior', 'A close-up moving image of a mouth is projected onto the back wall beside an illuminated doorway and the sculptural brain.'),
    ]
    figures = []
    for position, (slug, title, alt) in enumerate(images, start=1):
        figures.append(f'<figure><a class="image-link" href="../../assets/art/{slug}-1600.webp" data-view-image data-caption="{title}" aria-label="Enlarge: {title}">{image(slug, alt, "../../", lazy=position != 1, sizes="92vw" if position == 1 else "(max-width: 600px) 92vw, 45vw")}</a><figcaption><span>{title}</span><span>{position:02d} / 03</span></figcaption></figure>')
    content = heading('Whoop Dee Doo / Portland', 'TBA installation', 'A room for the brain.', 'An interactive installation for the Time-Based Art Festival, presented through Whoop Dee Doo.')
    content += '<div class="wrap"><div class="series-intro"><p>Part of a larger Whoop Dee Doo environment themed around the body, this room imagined the brain as a space visitors could enter. A sculptural brain could be manipulated to control projected “memories.” Arduino, tilt switches, Max/MSP, and found video connected the object to the changing image. Discarded materials—including carpet, trash bags, and metallic bowls—formed the surrounding room.</p><dl class="series-meta"><div><dt>Project</dt><dd>Whoop Dee Doo / TBA, Portland</dd></div><div><dt>Interactive system</dt><dd>Roger Link</dd></div><div><dt>Room design</dt><dd>Roger Link with Natalie Myers and Chris Beer</dd></div><div><dt>Photographs</dt><dd>Roger Link</dd></div></dl></div>'
    content += f'<div class="gallery">{"".join(figures)}</div><nav class="series-pagination" aria-label="Related work"><a href="../">← Whoop Dee Doo</a><a href="../../works/">Visual archive →</a></nav></div>'
    content += '<dialog class="viewer" id="viewer" aria-label="Project photograph viewer"><div class="viewer-layout"><div class="viewer-top"><span data-view-position aria-live="polite"></span><button type="button" data-view-close autofocus>Close ×</button></div><figure><img src="" alt=""></figure><div class="viewer-bottom"><span data-view-caption></span><div class="viewer-controls"><button type="button" data-view-previous aria-label="Previous image">← Previous</button><button type="button" data-view-next aria-label="Next image">Next →</button></div></div></div></dialog>'
    write('whoop-dee-doo/tba/index.html', document('TBA installation — Whoop Dee Doo', 'An interactive brain-themed environment for TBA in Portland, made through Whoop Dee Doo. Project photographs by Roger Link.', content, '../../', 'Works'))
    images = [
        ('baltimore-performance', 'Performance / constructed set', 'Costumed performers gather around a green-covered table inside a white Whoop Dee Doo set, beneath a large sculptural face.'),
        ('baltimore-audience', 'Audience', 'An audience wearing red-and-blue glasses watches the show; several people wear bright costumes and face paint.'),
        ('baltimore-roger', 'In the room / Roger Link in black', 'Roger Link, in black beside a tall blue-costumed figure, among participants and audience members inside the Baltimore show.'),
    ]
    figures = []
    for position, (slug, title, alt) in enumerate(images, start=1):
        figures.append(f'<figure><a class="image-link" href="../../assets/art/{slug}-1600.webp" data-view-image data-caption="{title}" aria-label="Enlarge: {title}">{image(slug, alt, "../../", lazy=position != 1, sizes="92vw" if position == 1 else "(max-width: 600px) 92vw, 45vw")}</a><figcaption><span>{title}</span><span>{position:02d} / 03</span></figcaption></figure>')
    content = heading('Whoop Dee Doo / Baltimore', 'Baltimore show', 'A set becomes a gathering.', 'Selected show documentation. Further project details and credits to follow.')
    content += '<div class="wrap"><div class="series-intro"><p>A Whoop Dee Doo show in Baltimore. These three photographs move from the constructed set and performance to the audience, then back into the shared room. Roger Link appears in black in the final photograph.</p><dl class="series-meta"><div><dt>Project</dt><dd>Whoop Dee Doo</dd></div><div><dt>Location</dt><dd>Baltimore</dd></div><div><dt>Documentation</dt><dd>Performance / Audience / In the room</dd></div><div><dt>Archive</dt><dd><a href="../">Whoop Dee Doo ↗</a></dd></div></dl></div>'
    content += f'<div class="gallery">{"".join(figures)}</div><nav class="series-pagination" aria-label="Related projects"><a href="../">← Whoop Dee Doo</a><a href="../tba/">TBA installation →</a></nav></div>'
    content += '<dialog class="viewer" id="viewer" aria-label="Project photograph viewer"><div class="viewer-layout"><div class="viewer-top"><span data-view-position aria-live="polite"></span><button type="button" data-view-close autofocus>Close ×</button></div><figure><img src="" alt=""></figure><div class="viewer-bottom"><span data-view-caption></span><div class="viewer-controls"><button type="button" data-view-previous aria-label="Previous image">← Previous</button><button type="button" data-view-next aria-label="Next image">Next →</button></div></div></div></dialog>'
    write('whoop-dee-doo/baltimore/index.html', document('Baltimore show — Whoop Dee Doo', 'Three photographs of a Whoop Dee Doo show in Baltimore: performance, audience, and Roger Link in the room.', content, '../../', 'Works'))


def main():
    home()
    works()
    series()
    recordings()
    about()
    unfold()
    experiments()
    whoop_dee_doo()
    missing = heading('CF / 404', 'Not here<span style="color:var(--rust)">.</span>', 'A different path, perhaps.')
    missing += '<div class="wrap"><div class="prose"><p>This page is not in the Index. Return to the recordings, follow a visual collection, or start again.</p><a class="editorial-link" href="/">Back to the Index <span aria-hidden="true">↗</span></a></div></div>'
    write('404.html', document('Page not found', 'This page is not in the Cancelled Futures Index.', missing, '/'))
    print(f'Rendered homepage, archive, {len(COLLECTIONS)} series, recordings, album, About, and Unfold.')


if __name__ == '__main__':
    main()
