from soundcloud import Client
import os

CLIENT_ID = os.environ.get('SOUNDCLOUD_ID')
CLIENT_SECRET = os.environ.get('SOUNDCLOUD_SECRET')
CLIENT_EMAIL = os.environ.get('SOUNDCLOUD_EMAIL')
CLIENT_PASSWORD = os.environ.get('SOUNDCLOUD_PASSWORD')

print CLIENT_ID
print CLIENT_EMAIL
print CLIENT_SECRET
print CLIENT_PASSWORD


client = Client(
    client_id=YOUR_CLIENT_ID,
)

    # client_secret=YOUR_CLIENT_SECRET,
    # username=CLIENT_USERNAME,
    # password=CLIENT_PASSWORD
