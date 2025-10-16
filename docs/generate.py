import csv
import os

# Créer le dossier docs/ s'il n'existe pas
os.makedirs('docs', exist_ok=True)

# Lire le template
with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Lire les chansons
with open('songs.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    songs = list(reader)

# Générer une page par chanson
for song in songs:
    html = template
    html = html.replace('{{TITLE}}', song['title'])
    html = html.replace('{{ARTIST}}', song['artist'])
    html = html.replace('{{NOTES}}', song['notes'])
    html = html.replace('{{DESCRIPTION}}', song['description'])
    html = html.replace('{{SLUG}}', song['slug'])
    
    filename = f"docs/{song['slug']}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Créé : {filename}")

print(f"\n🎉 {len(songs)} pages générées dans docs/")
