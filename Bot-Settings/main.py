from bot-settings.py import *
from tkinter import *

# Define the function to run
def main():
    """
    This is the main function that runs the Twitter bot.
    """
    # Follow back accounts who follow me immediately
    follow_back_followers()

    # Tweet something everyday
    tweet_something_daily()

    # Schedule a tweet
    schedule_tweet()

# Run the function
main()
