from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from pymongo import MongoClient
import json

MONGO_HOST= 'mongodb://localhost/twitterdb' 

class StdOutListener(StreamListener):
	def on_data(self, data):
		try:
			client = MongoClient(MONGO_HOST)
			db = client.twitterdb
			datajson = json.loads(data)
			db.twitter_search.insert(datajson)
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
	tracklist = ['remdesivir', 'chloroquine', 'hydroxychloroquine']
	GEOBOX_USA = [-125,25.1,-60.5,49.1]	
	stream = Stream(auth,l, ) 
	#filter based on geo location or keywords
        stream.filter(track = tracklist,locations = GEOBOX_USA, languages=['en'])
	


