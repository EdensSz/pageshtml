import csv
import re
import os
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

def scan_blog_pages(blog_dir='blog'):
    """Scan le dossier blog/ et retourne la liste des slugs"""
    blog_pages = []
    
    if not os.path.exists(blog_dir):
        print(f"⚠️  Dossier {blog_dir}/ n'existe pas encore")
        return blog_pages
    
    for item in os.listdir(blog_dir):
        item_path = os.path.join(blog_dir, item)
        
        # Vérifie si c'est un dossier contenant index.html
        if os.path.isdir(item_path):
            index_path = os.path.join(item_path, 'index.html')
            if os.path.exists(index_path):
                blog_pages.append(item)
        
        # Ou si c'est un fichier HTML direct
        elif item.endswith('.html') and item != 'index.html':
            slug = item.replace('.html', '')
            blog_pages.append(slug)
    
    return blog_pages

# Configuration
base_url = "https://song.pianomaker.art"
today = datetime.now().strftime('%Y-%m-%d')

# Lire les chansons du CSV
songs = []
if os.path.exists('songs.csv'):
    with open('songs.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        songs = list(reader)
    print(f"✅ {len(songs)} chansons chargées depuis CSV")
else:
    print("⚠️  songs.csv introuvable")

# Scanner les pages blog
blog_pages = scan_blog_pages('blog')
print(f"✅ {len(blog_pages)} pages blog trouvées")

# Générer le sitemap
sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

# 1. Homepage (priorité maximale)
sitemap += f'''  <url>
    <loc>{base_url}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
'''

# 2. Blog Hub Page (si existe)
if os.path.exists('blog/index.html') or os.path.exists('blog'):
    sitemap += f'''  <url>
    <loc>{base_url}/blog/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
'''

# 3. Pages Blog (priorité haute)
for slug in sorted(blog_pages):
    sitemap += f'''  <url>
    <loc>{base_url}/blog/{slug}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''

# 4. Pages de chansons (priorité normale)
for song in songs:
    song_name = song['song_name'].strip()
    slug = slugify(song_name)
    
    sitemap += f'''  <url>
    <loc>{base_url}/{slug}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''

sitemap += '</urlset>'

# Sauvegarder
os.makedirs('docs', exist_ok=True)
with open('docs/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

# Résumé
total_urls = 1 + (1 if blog_pages else 0) + len(blog_pages) + len(songs)
print(f"\n📄 Sitemap créé avec {total_urls} URLs:")
print(f"   - 1 homepage")
print(f"   - 1 blog hub" if blog_pages else "   - 0 blog hub")
print(f"   - {len(blog_pages)} pages blog")
print(f"   - {len(songs)} chansons")
print(f"\n✅ Fichier sauvegardé: docs/sitemap.xml")
