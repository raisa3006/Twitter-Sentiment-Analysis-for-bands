from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#variables that contain user credentials to access twitter API
access_token = "57013255-vkV7WrKiBxIANH8VAB5ovNHYqWuwSAj6NuHzpr4Km"
access_token_secret = "9zNVkciWGRE1BM4eRb340AO1FZJFt898PgtGl4siRQAgL"
consumer_key = "GiYqPnKU8l8gMDZh5n9S5HC9j"
consumer_secret = "Yf06FAaRqUItEpRwElguc8kfwluDGE2gWaasNc2S33EmT4T3YE"

#this is the basic listener that just prints received tweets to stdout
class StdOutListener(StreamListener):
    
    def on_data(self,data):
        with open("c:/dellbackup/all things data science/datasets/twitter_data_bands.txt","a") as tf:
            tf.write(data)
        return True
        
    def on_error(self,status):
        print status
        
if __name__ == "__main__":
    #handling the twitter authentication and the connection to the twitter's streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)
    
    #this line will filter Twitter streams tp capture data by keywords, :coldplay,beatles,u2
    stream.filter(track=["coldplay","beatles","u2"])
    
    