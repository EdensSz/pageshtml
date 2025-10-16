<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- PRIMARY SEO -->
  <title>{{ song_name }} Piano Sheet Music - {{ artist_name }} | Free PDF & Tutorial</title>
  <meta name="description" content="Learn {{ song_name }} by {{ artist_name }} on piano. Free sheet music PDF, video tutorial, and step-by-step guide for beginners. Start playing today!">
  
  <!-- KEYWORDS (low priority but helps) -->
  <meta name="keywords" content="{{ song_name }} piano, {{ artist_name }} piano tutorial, {{ song_name }} sheet music, piano notes {{ song_name }}, how to play {{ song_name }}, {{ song_name }} piano chords">
  
  <!-- CANONICAL -->
  <link rel="canonical" href="https://song.pianomaker.art/{{ slug }}.html">
  
  <!-- OPEN GRAPH (Facebook, LinkedIn, WhatsApp) -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="PianoMaker">
  <meta property="og:title" content="{{ song_name }} - {{ artist_name }} | Piano Tutorial">
  <meta property="og:description" content="Free piano sheet music and video tutorial. Learn to play {{ song_name }} step-by-step.">
  <meta property="og:url" content="https://song.pianomaker.art/{{ slug }}.html">
  <meta property="og:image" content="https://song.pianomaker.art/assets/og-{{ slug }}.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  
  <!-- TWITTER CARD -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@PianoMaker">
  <meta name="twitter:title" content="{{ song_name }} Piano Tutorial - {{ artist_name }}">
  <meta name="twitter:description" content="Free sheet music PDF + video tutorial. Learn {{ song_name }} on piano today!">
  <meta name="twitter:image" content="https://song.pianomaker.art/assets/og-{{ slug }}.jpg">
  
  <!-- PRECONNECT (Speed Optimization) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://pianomaker.art">
  <link rel="dns-prefetch" href="https://www.youtube.com">
  
  <!-- SCHEMA.ORG - MusicComposition -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "MusicComposition",
    "name": "{{ song_name }}",
    "composer": {
      "@type": "Person",
      "name": "{{ artist_name }}"
    },
    "description": "{{ description }}",
    "url": "https://song.pianomaker.art/{{ slug }}.html",
    "genre": "Piano Sheet Music",
    "inLanguage": "en",
    "musicalKey": "{{ key }}",
    "datePublished": "{{ date }}",
    "publisher": {
      "@type": "Organization",
      "name": "PianoMaker",
      "url": "https://pianomaker.art"
    }
  }
  </script>
  
  <!-- SCHEMA.ORG - HowTo (for tutorial aspect) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "How to Play {{ song_name }} on Piano",
    "description": "Step-by-step tutorial to learn {{ song_name }} by {{ artist_name }} on piano",
    "image": "https://song.pianomaker.art/assets/og-{{ slug }}.jpg",
    "totalTime": "PT15M",
    "estimatedCost": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": "0"
    },
    "supply": [
      {
        "@type": "HowToSupply",
        "name": "Piano or Keyboard"
      }
    ],
    "tool": [
      {
        "@type": "HowToTool",
        "name": "Sheet Music PDF"
      }
    ],
    "step": [
      {
        "@type": "HowToStep",
        "name": "Download Sheet Music",
        "text": "Get the free PDF sheet music for {{ song_name }}",
        "url": "https://song.pianomaker.art/{{ slug }}.html"
      },
      {
        "@type": "HowToStep",
        "name": "Watch Video Tutorial",
        "text": "Follow along with the step-by-step video tutorial"
      },
      {
        "@type": "HowToStep",
        "name": "Practice Hands Separately",
        "text": "Master the right hand and left hand parts individually"
      },
      {
        "@type": "HowToStep",
        "name": "Play Both Hands Together",
        "text": "Combine both hands slowly and gradually increase tempo"
      }
    ]
  }
  </script>
  
  <!-- SCHEMA.ORG - BreadcrumbList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://pianomaker.art"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Piano Tutorials",
        "item": "https://song.pianomaker.art"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "{{ song_name }}",
        "item": "https://song.pianomaker.art/{{ slug }}.html"
      }
    ]
  }
  </script>

  <!-- INLINE CRITICAL CSS -->
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
      color: #1a1a1a;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      padding: 20px;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      background: #fff;
      border-radius: 16px;
      padding: 48px 32px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.15);
    }
    
    /* HEADER */
    h1 {
      font-size: clamp(1.75rem, 5vw, 2.75rem);
      font-weight: 700;
      margin-bottom: 8px;
      color: #667eea;
      text-align: center;
      line-height: 1.2;
    }
    .artist {
      font-size: 1.25rem;
      color: #666;
      text-align: center;
      margin-bottom: 24px;
      font-weight: 500;
    }
    .description {
      font-size: 1.125rem;
      color: #444;
      text-align: center;
      margin-bottom: 32px;
      line-height: 1.7;
    }
    
    /* CTA BUTTON */
    .cta {
      display: block;
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: white;
      text-align: center;
      padding: 18px 48px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      font-size: 1.125rem;
      margin: 32px auto;
      max-width: 400px;
      box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
      transition: all 0.3s ease;
    }
    .cta:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(102, 126, 234, 0.5);
    }
    
    /* FEATURES GRID */
    .features {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 24px;
      margin: 48px 0;
    }
    .feature {
      background: #f8f9ff;
      padding: 24px;
      border-radius: 12px;
      text-align: center;
      border: 2px solid #e8ebff;
    }
    .feature-icon {
      font-size: 2.5rem;
      margin-bottom: 12px;
    }
    .feature h3 {
      font-size: 1.125rem;
      color: #667eea;
      margin-bottom: 8px;
    }
    .feature p {
      color: #666;
      font-size: 0.95rem;
    }
    
    /* FAQ SECTION */
    .faq {
      margin-top: 64px;
      padding-top: 48px;
      border-top: 2px solid #e8ebff;
    }
    .faq h2 {
      font-size: 2rem;
      color: #667eea;
      text-align: center;
      margin-bottom: 32px;
    }
    .faq-item {
      margin-bottom: 24px;
      background: #f8f9ff;
      padding: 24px;
      border-radius: 12px;
      border-left: 4px solid #667eea;
    }
    .faq h3 {
      font-size: 1.125rem;
      color: #1a1a1a;
      margin-bottom: 12px;
      font-weight: 600;
    }
    .faq p {
      color: #444;
      line-height: 1.7;
    }
    
    /* FOOTER */
    footer {
      text-align: center;
      margin-top: 64px;
      padding-top: 32px;
      border-top: 2px solid #e8ebff;
      color: #666;
    }
    footer a {
      color: #667eea;
      text-decoration: none;
      font-weight: 500;
    }
    footer a:hover {
      text-decoration: underline;
    }
    
    /* MOBILE OPTIMIZATION */
    @media (max-width: 640px) {
      .container {
        padding: 32px 20px;
      }
      .cta {
        padding: 16px 32px;
        font-size: 1rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- HEADER WITH H1 -->
    <header>
      <h1>{{ song_name }}</h1>
      <p class="artist">by {{ artist_name }}</p>
      <p class="description">{{ description }}</p>
    </header>

    <!-- PRIMARY CTA -->
    <a href="https://pianomaker.art/song/{{ slug }}" class="cta">
      🎹 Start Learning Now - Free!
    </a>

    <!-- FEATURES SECTION -->
    <section class="features">
      <div class="feature">
        <div class="feature-icon">📄</div>
        <h3>Free PDF Sheet Music</h3>
        <p>Download high-quality piano sheet music instantly</p>
      </div>
      <div class="feature">
        <div class="feature-icon">🎥</div>
        <h3>Video Tutorial</h3>
        <p>Step-by-step video guide for all skill levels</p>
      </div>
      <div class="feature">
        <div class="feature-icon">🎵</div>
        <h3>Easy Piano Notes</h3>
        <p>Simplified arrangement perfect for beginners</p>
      </div>
    </section>

    <!-- FAQ SECTION (SEO GOLDMINE) -->
    <section class="faq">
      <h2>Frequently Asked Questions</h2>
      
      <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h3 itemprop="name">How do I learn {{ song_name }} on piano?</h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">Start by downloading the free sheet music PDF, then watch our video tutorial. Practice the right hand and left hand separately before combining them. With regular practice, you can master {{ song_name }} by {{ artist_name }} in just a few weeks!</p>
        </div>
      </div>

      <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h3 itemprop="name">Is {{ song_name }} difficult to play on piano?</h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">{{ song_name }} by {{ artist_name }} is suitable for intermediate players. Our simplified arrangement makes it accessible for beginners while keeping the iconic melody intact. The video tutorial breaks down each section to make learning easier.</p>
        </div>
      </div>

      <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h3 itemprop="name">Where can I download {{ song_name }} piano sheet music for free?</h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">You can download the free PDF sheet music for {{ song_name }} directly from PianoMaker. Click the button above to access the sheet music, video tutorial, and step-by-step guide instantly.</p>
        </div>
      </div>

      <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h3 itemprop="name">What are the piano chords for {{ song_name }}?</h3>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">The piano chords for {{ song_name }} by {{ artist_name }} are included in our free sheet music PDF. The tutorial also demonstrates proper finger positioning and chord transitions to help you play smoothly.</p>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer>
      <p>© 2024 <a href="https://pianomaker.art">PianoMaker.art</a> - Learn Piano Online</p>
      <p style="margin-top: 12px;">
        <a href="https://pianomaker.art/library">Browse More Piano Tutorials</a> | 
      </p>
    </footer>
  </div>

  <!-- REDIRECTION SCRIPT (non-blocking) -->
  <script>
    setTimeout(function() {
      window.location.href = 'https://pianomaker.art/song/{{ slug }}';
    }, 3000);
  </script>
</body>
</html>
