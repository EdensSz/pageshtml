import csv
import os
import re
from urllib.parse import quote

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text.strip('-')

def generate_pages(csv_file, template_file, output_dir):
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            song_name = row['song_name'].strip()
            artist_name = row.get('artist_name', 'Unknown Artist').strip()
            
            slug = slugify(song_name)
            song_encoded = quote(song_name)
            
            html = template.replace('{{SONG_NAME}}', song_name)
            html = html.replace('{{ARTIST_NAME}}', artist_name)
            html = html.replace('{{SONG_SLUG}}', slug)
            html = html.replace('{{SONG_NAME_ENCODED}}', song_encoded)
            
            output_path = os.path.join(output_dir, f'{slug}.html')
            with open(output_path, 'w', encoding='utf-8') as out:
                out.write(html)
            
            print(f"✅ {slug}.html")

def generate_sitemap(csv_file, output_file='sitemap.xml'):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        urls = []
        for row in reader:
            song_name = row['song_name'].strip()
            slug = slugify(song_name)
            urls.append(f"https://song.pianomaker.art/{slug}")
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in urls:
        sitemap += f'  <url>\n'
        sitemap += f'    <loc>{url}</loc>\n'
        sitemap += f'    <changefreq>monthly</changefreq>\n'
        sitemap += f'    <priority>0.8</priority>\n'
        sitemap += f'  </url>\n'
    
    sitemap += '</urlset>'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    
    print("✅ sitemap.xml")

if __name__ == '__main__':
    generate_pages('songs.csv', 'template.html', 'docs')
    generate_sitemap('songs.csv', 'docs/sitemap.xml')
    
    # Créer robots.txt
    with open('docs/robots.txt', 'w') as f:
        f.write('User-agent: *\n')
        f.write('Allow: /\n\n')
        f.write('Sitemap: https://song.pianomaker.art/sitemap.xml\n')
    
    print("✅ robots.txt")
    print("\n🎉 Terminé ! Dossier 'docs' créé avec toutes les pages")
