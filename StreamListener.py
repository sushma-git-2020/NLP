from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json

class StdOutListener(StreamListener):
	def on_data(self, data):
		try:
			with open('covid19.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" %str(e))
		return True

	def on_error(self, status):
		print("Encountered error during streaming: ", status_code)
		sys.exit()

if __name__ == '__main__':
	config_file = ".tweepy.json"
	with open(config_file) as fh:
		config = json.load(fh)
	l = StdOutListener()
	auth = OAuthHandler(config['consumer_key'],config['consumer_secret'])
	auth.set_access_token(config['access_token'], config['access_token_secret'])
	tracklist = ['Covid-19', 'coronavirus']
	stream = Stream(auth,l) 
	stream.filter(track = tracklist, languages=['en'])
	


