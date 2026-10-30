"""Generate the static GitHub Pages site from the approved article catalog."""
from pathlib import Path
from html import escape as e
import json

ROOT=Path(__file__).resolve().parents[1]
ARTICLES=json.loads((ROOT/'content/articles.json').read_text())
CATEGORIES=[('profiles','Profiles'),('travel-and-adventure','Travel and Adventure'),('science-environment-and-culture','Science, Environment and Culture')]
NAMES=dict(CATEGORIES)
BIO='<p>Lolly Merrell is a writer, journalist, and editor specializing in immersive reporting and narrative storytelling about science, the environment, travel, and compelling personalities.</p><p>After earning her master’s degree from Northwestern University’s Medill School of Journalism, Merrell worked on staff at several publications, including <em>Outside</em>, <em>Snow Country</em>, and <em>High Country News</em>. Her reporting assignments have taken her to Rajasthani tiger country, underground caves in Belize, a 16,000-ft-high glaciologists’ camp in Alaska, and the Rustic Roads of Wisconsin.</p>'

def branding(prefix='',footer=False):
 name='<span class="brand-name">Lolly Merrell</span>' if footer else '<h1 class="brand-name">Lolly Merrell</h1>'
 return f'<div class="site-branding"><a class="brand" href="{prefix or "./"}" aria-label="Lolly Merrell home">{name}<p class="site-description">Writer / Journalist / Editor</p></a></div>'

def document(title,body,path='',prefix='',description='',image='assets/images/dolomites.webp',home=False,article=False):
 name=e(title+' | Lolly Merrell' if title else 'Lolly Merrell | Writer, Journalist & Editor')
 desc=e(description or 'Lolly Merrell is a writer, journalist, and editor specializing in immersive reporting and narrative storytelling about science, the environment, travel, and compelling personalities.',quote=True)
 header=branding(prefix) if home else branding(prefix).replace('<h1 class="brand-name">','<span class="brand-name">').replace('</h1>','</span>')
 return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}</title><meta name="description" content="{desc}">
<link rel="canonical" href="https://lollymerrell.com/{path}">
<meta property="og:title" content="{name}"><meta property="og:description" content="{desc}"><meta property="og:type" content="{'website' if home or path.startswith('publications/category') else 'article'}"><meta property="og:url" content="https://lollymerrell.com/{path}"><meta property="og:image" content="https://lollymerrell.com/{image}"><meta name="theme-color" content="#265b8b">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/styles.css">
</head><body><a class="skip-link" href="#main">Skip to content</a>
<header>{header}</header>{body}
<footer class="site-footer">{"" if article else branding(prefix,True)}<p class="copyright">© 2026 Lolly Merrell. All rights reserved.</p></footer>
</body></html>'''

def card(a,prefix=''):
 return f'''<article class="home-post"><a href="{prefix}publications/{a['slug']}/"><div class="post-image"><img src="{prefix}{a['thumbnail']}" alt="" width="540" height="720" loading="lazy"><span class="post-category">{e(a['publication'])}</span></div><div class="post-content"><h4 class="post-title">{e(a['title'])}</h4></div></a></article>'''

def cards(articles,prefix=''):
 return '<div class="home-posts">'+''.join(card(a,prefix) for a in articles)+'</div>'

def save(path,html):
 target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(html+'\n')

sections=''
for cat,title in CATEGORIES:
 subset=[a for a in ARTICLES if a['category']==cat]
 sections+=f'<section class="work-category" id="{cat}" aria-labelledby="{cat}-title"><h3 id="{cat}-title">{title}</h3>{cards(subset)}</section>'
body=f'''<main id="main"><section class="hero" aria-label="About Lolly"><picture><img class="hero-image" src="assets/images/dolomites.webp" alt="A hiker descending a trail toward a mountain refuge beneath the Dolomites" width="1950" height="2600" fetchpriority="high"></picture><div class="hero-content"><div class="hero-copy">{BIO}<a class="btn btn-white" href="mailto:lollymerrell@gmail.com">Contact Lolly</a></div></div></section>
<div class="page-width"><section aria-labelledby="featured-title"><h2 class="publications-heading" id="featured-title">Featured Work</h2>{sections}</section></div>
<section class="contact" id="contact" aria-labelledby="contact-title"><h2 id="contact-title">Contact</h2><a class="btn btn-white" href="mailto:lollymerrell@gmail.com">Contact Lolly</a></section></main>'''
save(Path('index.html'),document('',body,home=True))
paths=['']
for cat,title in CATEGORIES:
 path=f'publications/category/{cat}/';prefix='../../../'
 body=f'<main class="page-width archive-page" id="main"><header class="archive-header"><a class="archive-back" href="{prefix}#{cat}">← Back to selected work</a><h1>{title}</h1></header>{cards([a for a in ARTICLES if a["category"]==cat],prefix)}</main>'
 # Category cards use level 2 below the page's level 1.
 body=body.replace('<h4 class="post-title">','<h2 class="post-title">').replace('</h4>','</h2>')
 save(Path(path)/'index.html',document(title,body,path,prefix));paths.append(path)
for i,a in enumerate(ARTICLES):
 prefix='../../';path=f'publications/{a["slug"]}/';category=NAMES[a['category']]
 prev=ARTICLES[(i-1)%len(ARTICLES)];nxt=ARTICLES[(i+1)%len(ARTICLES)]
 body=f'''<main id="main"><article class="article"><header><h1>{e(a['title'])}</h1><p class="article-byline">by Lolly Merrell | {e(a['publication'])}</p></header><div class="article-layout"><a class="article-preview" href="{prefix}{a['pdf']}" aria-label="View PDF of {e(a['title'])}"><img src="{prefix}{a['image']}" alt="Opening page of {e(a['title'])}" width="{a['image_width']}" height="{a['image_height']}"></a><div class="article-description"><p>{e(a['summary'])}</p><a class="btn" href="{prefix}{a['pdf']}">View PDF here »</a><span class="pdf-size">PDF · {a['mb']:.1f} MB</span><a href="{prefix}#{a['category']}">← Back to {category}</a></div></div><div class="tags"><a href="../category/{a['category']}/">{e(category)}</a></div></article><nav class="post-navigation" aria-label="Article navigation"><a href="../{prev['slug']}/">Previous: {e(prev['title'])}</a><a href="../{nxt['slug']}/">Next: {e(nxt['title'])}</a></nav></main>'''
 save(Path(path)/'index.html',document(a['title'],body,path,prefix,description=a['summary'],image=a['image'],article=True));paths.append(path)
body='<main class="page-width not-found" id="main"><h1>Page not found</h1><p>The page may have moved. Explore Lolly’s selected work or get in touch.</p><a class="btn" href="/">Return to the home page</a></main>'
save(Path('404.html'),document('Page not found',body,prefix='/'))
save(Path('sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>https://lollymerrell.com/{p}</loc></url>' for p in paths)+'</urlset>')
print(f'Built homepage, {len(CATEGORIES)} category pages, and {len(ARTICLES)} article pages.')
