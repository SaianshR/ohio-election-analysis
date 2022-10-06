import tweepy
import pandas as pd

CONSUMER_KEY = 'VfVZrZ7ZE2UiuOzN5g88NnnkR'
CONSUMER_SECRET = 'KVB7AfaGIGbtkRleZJzAvIQGHwJCtLdW9HjcMbsg7DX9yvx4bo'
ACCESS_TOKEN = '1032810058499977216-UPvZCCC6pEwCejo4VEvkDapbmsVWNx'
ACCESS_TOKEN_SECRET = 'gSX1uu7P5e6jDx2VO7419hrshfnUML2jS26uFoUInZ7Cn'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPoxhgEAAAAAYD5BGdQ7VTHjIVLwgIFe2Gqmm9E%3DTjjm1sOksV4G4ybHMWUln9y512w6XkIbHIx3CwUfu8k3Or97he'

def auth(hashtag):
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit = True)

    except BaseException as e:
        print("An error occurred during the authentication:", e)

    try:
        tweets = tweepy.Cursor(api.search_tweets, q= hashtag).items(3000)

        df = pd.DataFrame(columns=['id', 'created_at', 'username', 'location', 'following',
                                'followers', 'retweetcount','favorite', 'text'])

        for tweet in tweets:
            id = tweet.id_str
            created_at = tweet.created_at
            username = tweet.user.screen_name
            location = tweet.user.location
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            favorite = tweet.favorite_count
            retweetcount = tweet.retweet_count
            text = tweet.text

            tweets_formatted = [id, created_at, username, location, following,
                        followers, retweetcount, favorite, text]

            df.loc[len(df)] = tweets_formatted
    except BaseException as e:
        print("An error occurred during the scraping:", str(e))

    return df

## Candidates: J.D. Vance & Tim Ryan

## Hashtags to try:
'''
Ohio Senate Race Hashtags:
- #OHSen (1,2,3,7, 8)

Tim Ryan Hashtags:
- #TimRyan (4)
- #Vets4Tim
- #TimRyanForSenate
- #RepublicansForTimRyan
- #VoteTimeRyan

JD Vance Hashtags:
- #JDVance (5)
- #VoteJDVance (6)

Non-hashtag searches:
- Ohio Senate race (9)
- Tim Ryan (10)
- JD Vance (11)
'''

# Running function to scrape tweets
# ohTweets = auth('OHSen')
ohTweets = auth('JD Vance')
# ohTweets = auth('JDVance')

# Saving tweets to a csv file
ohTweets.to_csv('OhioTweets11.csv')