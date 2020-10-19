import tweepy

# Authenticate to Twitter
api_public = ""
api_secret = ""
token_public = ""
token_secret = ""

auth = tweepy.OAuthHandler(api_public, api_secret)
auth.set_access_token(token_public, token_secret)


# Create API object
api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")


# Create a tweet
# api.update_status("Hello Tweepy")


##################################################################

# user = api.get_user("GordoMonstruo")
# print(user.status.text)


# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)
# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)


# api.create_friendship("realpython")

# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# print(f"Tweet: {tweets[0]}")   mucha data

# api.create_favorite(tweet.id)


# tweets = api.mentions_timeline()
# for tweet in tweets:
#     tweet.favorite()
#     tweet.user.follow()

# texts = str(tweets).split("text': ")
# for text in texts:
#     print(f"{text}\n")

# for tweet in tweepy.Cursor(api.home_timeline).items(100):
#     print(f"{tweet.user.name} said: {tweet.text}")


