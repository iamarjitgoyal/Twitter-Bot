# Twitter Bot

This is a Python script that implements a Twitter bot using the Tweepy library. The bot can perform the following actions:

- Reply to a tweet with a relevant GIF or image
- Retweet popular tweets related to a given query
- Follow back accounts that follow the bot immediately
- Tweet something every day
- Schedule a tweet for a specific date and time

## Setup

To set up the Twitter bot, follow these steps:

1. Clone this repository to your local machine.
2. Install the required packages listed in the `requirements.txt` file using the following command:
    ``` pip install -r requirements.txt ```

3. Create a Twitter account and apply for [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access).
4. Create a new [Twitter app](https://developer.twitter.com/en/apps) and generate API keys and access tokens.
5. Create a `config.py` file and add your API credentials:

``` 
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
GIPHY_API_KEY = 'your_giphy_api_key'
```

6. Create a `Bot-settings.py` file and modify the bot settings as per your requirements.
7. Run the script using the following command:

```
python bot.py
```


## Usage

The Twitter bot can be customized by modifying the settings in the `Bot-settings.py` file. You can change the following settings:

- `QUERY`: The keyword or phrase to search for when retweeting popular tweets.
- `COUNT`: The number of popular tweets to retweet.
- `FOLLOW_BACK`: A boolean value that determines whether to follow back accounts that follow the bot immediately.
- `DAILY_TWEET`: A boolean value that determines whether to tweet something every day.
- `SCHEDULED_TWEET`: A boolean value that determines whether to schedule a tweet for a specific date and time.
- `SCHEDULED_DATE`: The date and time to schedule the tweet. 
