import soundcloud
import os

# Setup keys
client_id=os.environ.get('SOUNDCLOUD_ID')
client_secret=os.environ.get('SOUNDCLOUD_SECRET')
client_username = os.environ.get('SOUNDCLOUD_USERNAME')
client_password = os.environ.get('SOUNDCLOUD_PASSWORD')


tracks = client.get('/tracks', limit=10)
for track in tracks:
    print track.title
app = client.get('/apps/124')
print app.permalink_url