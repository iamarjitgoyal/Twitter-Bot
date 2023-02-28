import tweepy
import tk
import random
import requests
import datetime
from tkinter import *


# Set up the API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define the function to reply with a GIF or image
def reply_with_gif(tweet_id, query):
    # Search for a relevant GIF or image
    response = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key=your_giphy_api_key&tag={query}&rating=g")

    # Tweet the GIF or image
    if response.status_code == 200:
        media_id = api.media_upload(response.json()['data']['image_original_url']).media_id
        api.update_status(status='[GIF] ' + query, in_reply_to_status_id=tweet_id, media_ids=[media_id])

# Define the function to retweet popular tweets
def retweet_popular_tweets(query, count):
    # Search for popular tweets
    results = api.search(q=query, count=count, result_type='popular')

    # Retweet the popular tweets
    for result in results:
        api.retweet(result.id)
        print(f"Retweeted tweet {result.id}!")

# Define the function to follow back accounts who follow me immediately
def follow_back_followers():
    followers = api.followers()
    for follower in followers:
        if not follower.following:
            follower.follow()
            print(f"Followed back {follower.name}")

# Define the function to tweet something everyday
def tweet_something_daily():
    today = datetime.datetime.today()
    tweet = f"Good morning! Today is {today.strftime('%A, %B %d, %Y')}. Have a great day!"
    api.update_status(tweet)

# Define the function to schedule a tweet
def schedule_tweet():
    scheduled_date = datetime.datetime(2023, 2, 28, 15, 0, 0)  # Set the date and time to schedule the tweet
    tweet = "This tweet is scheduled for February 28th, 2023 at 3:00 PM!"
    api.update_status(tweet, scheduled_date)

# Define the function to run
def main():
    # Follow back accounts who follow me immediately
    follow_back_followers()

    # Tweet something everyday
    tweet_something_daily()

    # Schedule a tweet
    schedule_tweet()

# Run the function
main()
