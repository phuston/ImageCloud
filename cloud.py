from soundcloud import Client
import os

class CloudClient():

	def __init__():
		CLIENT_ID = os.environ.get('SOUNDCLOUD_ID')
		CLIENT_SECRET = os.environ.get('SOUNDCLOUD_SECRET')
		CLIENT_EMAIL = os.environ.get('SOUNDCLOUD_EMAIL')
		CLIENT_PASSWORD = os.environ.get('SOUNDCLOUD_PASSWORD')


		client = Client(
		    client_id=CLIENT_ID,
		 	client_secret=CLIENT_SECRET,
		    username=CLIENT_EMAIL,
		    password=CLIENT_PASSWORD
		)

	def post_track(filepath):
		track = client.post('/tracks', track={
		    'title': 'SampleTrack',
		    'sharing': 'private',
		    'asset_data': open(filepath, 'rb')
		})

   