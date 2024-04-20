import tweepy 

consumer_key = input("Enter your consumer key: ")
consumer_secret = input("Enter your consumer secret: ")
access_token = input("Enter your access token: ")
access_token_secret = input("Enter your access token secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

tweet_text = input("Enter the text for your tweet: ")
image_path = input("Enter the path of the media file: ")


status = api.update_with_media(image_path, tweet_text)
