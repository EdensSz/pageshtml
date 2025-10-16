import csv
import re
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

# Lire le CSV
with open('songs.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    songs = list(reader)

# Générer le sitemap
base_url = "https://edenssz.github.io/pageshtml"
today = datetime.now().strftime('%Y-%m-%d')

sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

for song in songs:
    song_name = song['song_name'].strip()
    slug = slugify(song_name)
    
    sitemap += f'''  <url>
    <loc>{base_url}/{slug}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''

sitemap += '</urlset>'

# Sauvegarder
with open('docs/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f"✅ Sitemap créé avec {len(songs)} URLs")
