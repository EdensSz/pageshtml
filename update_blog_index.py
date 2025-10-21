import os
import re
from datetime import datetime

def extract_metadata_from_html(filepath):
    """Extrait titre, date et description d'un fichier HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire le titre
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else os.path.basename(filepath).replace('.html', '')
    
    # Extraire la description (meta description)
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    excerpt = desc_match.group(1) if desc_match else "Click to read more about this topic..."
    
    # Utiliser la date de modification du fichier
    timestamp = os.path.getmtime(filepath)
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    return {
        'title': title,
        'excerpt': excerpt,
        'date': date,
        'icon': '🎹'
    }

def scan_blog_posts(post_dir='docs/blog/post'):
    """Scanne tous les articles HTML dans le dossier post/"""
    posts = []
    
    if not os.path.exists(post_dir):
        print(f"⚠️  Dossier {post_dir}/ n'existe pas")
        return posts
    
    for filename in os.listdir(post_dir):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(post_dir, filename)
            metadata = extract_metadata_from_html(filepath)
            metadata['file'] = filename
            posts.append(metadata)
            print(f"✓ Trouvé: {filename}")
    
    # Trier par date décroissante
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def generate_posts_js(posts):
    """Génère le code JavaScript pour le tableau posts"""
    js_code = "        const posts = [\n"
    
    for post in posts:
        # Échapper les guillemets dans le contenu
        title = post['title'].replace('"', '\\"')
        excerpt = post['excerpt'].replace('"', '\\"')
        
        js_code += f"""            {{
                title: "{title}",
                file: "{post['file']}",
                date: "{post['date']}",
                excerpt: "{excerpt}",
                icon: "{post['icon']}"
            }},
"""
    
    js_code += "        ];"
    return js_code

def update_blog_index(index_path='docs/blog/index.html', posts_js=''):
    """Met à jour l'index.html avec la nouvelle liste de posts"""
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer la section const posts = [...];
    pattern = r'const posts = \[.*?\];'
    updated_content = re.sub(pattern, posts_js, content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

# Exécution principale
print("🚀 Mise à jour de l'index du blog...\n")

posts = scan_blog_posts('docs/blog/post')
print(f"\n✅ {len(posts)} articles trouvés\n")

if posts:
    posts_js = generate_posts_js(posts)
    update_blog_index('docs/blog/index.html', posts_js)
    print("✅ Index mis à jour: docs/blog/index.html\n")
    
    print("📝 Articles indexés:")
    for post in posts:
        print(f"   - {post['title']} ({post['date']})")
else:
    print("⚠️  Aucun article trouvé dans docs/blog/post/")

print("\n💡 Mise à jour terminée!")
