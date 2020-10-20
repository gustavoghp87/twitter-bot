import tweepy
import logging
from config import create_api
import sys
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return            

        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                user = str(tweet).split("screen_name': '")[1].split("'")[0]
                id = str(tweet).split("id': ")[1].split(',')[0]
                print(f"\n\nEnviando mensaje a @{user}, id {id}")
                self.api.update_status(f"@{user} El listado de todos los maslazooms está en maslabook.com/maslazoom, saludos", id)
                # in_reply_to_status_id 
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        #if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
        #    try:
        #        tweet.retweet()
        #    except Exception as e:
        #        logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    #keywords = sys.argv
    #del keywords[0]
    #print("args:", str(keywords))
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["es"])

if __name__ == "__main__":
    main(["maslazoom", "maslazooms"])
    #os.execv(__file__, sys.argv)
    # Run a new iteration of the current script, providing any 
    # command line args from the current iteration
