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
            try:
                metadata = extract_metadata_from_html(filepath)
                metadata['file'] = filename
                posts.append(metadata)
                print(f"✓ Trouvé: {filename}")
            except Exception as e:
                print(f"⚠️  Erreur lors de la lecture de {filename}: {e}")
    
    # Trier par date décroissante
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def generate_posts_js(posts):
    """Génère le code JavaScript pour le tableau posts"""
    if not posts:
        return "        const posts = [];"
    
    js_code = "        const posts = [\n"
    
    for i, post in enumerate(posts):
        # Échapper les guillemets et backslashes dans le contenu
        title = post['title'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
        excerpt = post['excerpt'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
        
        # Pas de virgule après le dernier élément
        comma = "," if i < len(posts) - 1 else ""
        
        js_code += f"""            {{
                title: "{title}",
                file: "{post['file']}",
                date: "{post['date']}",
                excerpt: "{excerpt}",
                icon: "{post['icon']}"
            }}{comma}
"""
    
    js_code += "        ];"
    return js_code

def update_blog_index(index_path='docs/blog/index.html', posts_js=''):
    """Met à jour l'index.html avec la nouvelle liste de posts"""
    if not os.path.exists(index_path):
        print(f"⚠️  Fichier {index_path} introuvable")
        return False
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer la section const posts = [...];
        pattern = r'const posts = \[.*?\];'
        
        # Vérifier que le pattern existe
        if not re.search(pattern, content, flags=re.DOTALL):
            print("⚠️  Pattern 'const posts = [...]' non trouvé dans index.html")
            return False
        
        updated_content = re.sub(pattern, posts_js, content, flags=re.DOTALL)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"⚠️  Erreur lors de la mise à jour: {e}")
        return False

# Exécution principale
if __name__ == "__main__":
    print("🚀 Mise à jour de l'index du blog...\n")

    posts = scan_blog_posts('docs/blog/post')
    print(f"\n✅ {len(posts)} article(s) trouvé(s)\n")

    if posts:
        posts_js = generate_posts_js(posts)
        
        if update_blog_index('docs/blog/index.html', posts_js):
            print("✅ Index mis à jour: docs/blog/index.html\n")
            
            print("📝 Articles indexés:")
            for post in posts:
                print(f"   - {post['title'][:60]}... ({post['date']})")
        else:
            print("❌ Échec de la mise à jour de l'index")
    else:
        print("⚠️  Aucun article trouvé dans docs/blog/post/")
        print("💡 Assurez-vous que vos fichiers .html sont bien dans ce dossier")

    print("\n💡 Commitez et pushez sur GitHub pour voir les changements!")
