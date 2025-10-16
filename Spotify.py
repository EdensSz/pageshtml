import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os

# Tes playlists (remplace par tes IDs)
PLAYLISTS = [
    '37i9dQZF1DXcBWIGoYBM5M',
    '37i9dQZF1DX0XUsuxWHRQd',
]

# Connexion Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv('11f42530c10342e8b3a3ba72489b8e7b'),
    client_secret=os.getenv('f326233e7d71466583d05abf96c8c924')
))

# Récupérer toutes les tracks
tracks = []
for playlist_id in PLAYLISTS:
    results = sp.playlist_tracks(playlist_id)
    for item in results['items']:
        if item['track']:
            t = item['track']
            tracks.append({
                'song_name': t['name'],
                'artist_name': ', '.join([a['name'] for a in t['artists']]),
                'album': t['album']['name'],
                'url': t['external_urls']['spotify']
            })

# Sauvegarder en CSV
with open('spotify_tracks.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['song_name', 'artist_name', 'album', 'url'])
    writer.writeheader()
    writer.writerows(tracks)

print(f"✓ {len(tracks)} tracks sauvegardées")
