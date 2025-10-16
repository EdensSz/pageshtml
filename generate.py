import csv
import os
import re
from urllib.parse import quote

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

# Lire le template
with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Créer le dossier docs
os.makedirs('docs', exist_ok=True)

# Lire le CSV et générer les pages
with open('songs.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    songs = list(reader)

# Générer une page par chanson
for song in songs:
    song_name = song['song_name'].strip()
    artist_name = song.get('artist_name', 'Artiste inconnu').strip()
    
    slug = slugify(song_name)
    song_encoded = quote(song_name)
    
    html = template
    html = html.replace('{{SONG_NAME}}', song_name)
    html = html.replace('{{ARTIST_NAME}}', artist_name)
    html = html.replace('{{SONG_ENCODED}}', song_encoded)
    html = html.replace('{{SLUG}}', slug)
    
    filename = f"docs/{slug}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Créé : {filename}")

print(f"\n🎉 {len(songs)} pages générées dans docs/")
