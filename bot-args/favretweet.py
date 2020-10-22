from logging import log
import requests
import tweepy
import logging
from config import create_api
import time
import json
from decouple import config
#import sys
#import os
#import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

        starttime = time.time()
        while True:
            print(f"tick, son las {time.asctime(time.localtime(time.time()))}")
            url = 'https://maslabook.herokuapp.com/api/bot'
            payload = {'password': config('COUNTER_PW')}
            headers = {'content-type': 'application/json'}
            tuit = requests.post(url, data=json.dumps(payload), headers=headers)
            print(tuit.json())
            self.api.update_status(tuit.json())
            
            friends_names = []
            for friend in api.friends():
                friends_names.append(friend.screen_name)

            #print("Yo sigo:", friends_names)

            for follower in api.followers():
                if follower.screen_name not in friends_names:
                    try:
                        follower.follow()
                        api.create_mute(follower.screen_name)
                        print (f"Siguiendo a {follower.screen_name}, silenciado")
                    except:
                        print("\n")

            loop = 7200
            time.sleep(loop - ((time.time() - starttime) % loop))

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            print("This tweet is a reply or I'm its author so, ignore it")
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                user = str(tweet).split("screen_name': '")[1].split("'")[0]
                id = str(tweet).split("id': ")[1].split(',')[0]
                print(f"\n\nFaveado tuit {id} de @{user}")
            except Exception as e:
                #logger.error("Error on fav", exc_info=True)
                print("Ya faveado")

            try:
                text = str(tweet).split("text': '")[1].split("'")[0]
                print(text)
                user = str(tweet).split("screen_name': '")[1].split("'")[0]
                id = str(tweet).split("id': ")[1].split(',')[0]

                if 'maslazoom' in text.lower():
                    print(f"\n\nEnviando mensaje a @{user}, id {id}, por el tuit {text}")
                    self.api.update_status(f"@{user} El listado de todos los maslazooms está en maslabook.com/maslazoom, saludos", id)

                # if 'toalla' in text.lower() or 'toallin' in text.lower() or 'toallín' in text.lower():
                #     print(f"\n\nEnviando mensaje a @{user}, id {id}, por el tuit {text}")
                #     filename = 'temp.jpg'
                #     request = requests.get("https://i.pinimg.com/originals/40/a1/91/40a191c06187848f0a2070ad68555564.jpg", stream=True)
                #     if request.status_code == 200:
                #         with open(filename, 'wb') as image:
                #             for chunk in request:
                #                 image.write(chunk)
                #         self.api.update_with_media(filename, status=f"@{user} no olvides llevar una toalla")
                #         os.remove(filename)

            except Exception as e:
                logger.error("Error enviando mensaje", e)

        #if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
        #    try:
        #        tweet.retweet()
        #    except Exception as e:
        #        logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main():
    api = create_api()

    keywords = ["barranis", "barrani", "Barrani", "maslazoom", "maslazooms", "MaslaZoom", "Maslazoom", "MASLAZOOM"]
    #keywords = ["cochinchina"]
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["es"])

    #del keywords[0]
    #print("args:", str(keywords))

if __name__ == "__main__":
    main()
    #os.execv(__file__, sys.argv)
    # Run a new iteration of the current script, providing any 
    # command line args from the current iteration
