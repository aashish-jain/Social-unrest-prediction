import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def clean_df(df):
    """
    Input - A df of tweets
    Returns - A df that cleans the input 
             df and returns it.
    """
    rows_to_drop = []
    for i in range(len(df)):
        curr_row = df.iloc[i]
        
        if pd.isna(curr_row['id']):
            rows_to_drop.append(i)
        
        if (pd.isna(curr_row['full_text'])) or pd.isna(curr_row['created_at']) or not str(curr_row['created_at']).endswith("2019"):
            rows_to_drop.append(i)
        
        if curr_row['lang'] == '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>':
            rows_to_drop.append(i)
    print ("Dropping", len(rows_to_drop), "rows!")
    if len(rows_to_drop) == 0:
        return df
    return df.drop(rows_to_drop)


def get_sentiment(df):
    """
    Input - A dataframe of tweets from the CSV file.
    Returns - A df with an extra sentiment column.
    """
    vader = SentimentIntensityAnalyzer()
    
    tweets = df['full_text']

    tweet_ids = [str(int(x)) for x in df['id']]
    
    sentiment_dict = {}

    for i, tweet in enumerate(tweets):
        if tweet_ids[i] not in sentiment_dict:
            sentiment_dict[tweet_ids[i]] = vader.polarity_scores(tweet)

    neg, pos, neu, compound = [], [], [], []

    for i in range(len(df)):
        row = df.iloc[i]
        tweet_id = str(int(row['id']))
        sentiment = sentiment_dict[tweet_id]
        neg.append(sentiment['neg'])
        pos.append(sentiment['pos'])
        neu.append(sentiment['neu'])
        compound.append(sentiment['compound'])
    
    df['neg'] = neg
    df['neu'] = neu
    df['pos'] = pos
    df['compound'] = compound
    return df


def tweets_by_day(df, min_date=None, max_date=None):
    """
    Input - A df with created_at column
           converted by pd.to_datetime
    Returns - A dict with date as key and
             tweets on that date as values
    """
    if min_date is None:
        min_date = min(df['created_at']).date()
    
    if max_date is None:
        max_date = max(df['created_at']).date()
    
    date_dict = {}
    
    assert(max_date > min_date)
    
    date_range = pd.date_range(min_date, max_date)
    
    dates = [x.date() for x in df['created_at']]
    
    df['date'] = dates
    
    for date in dates:
        date_dict[str(date)] = df[df['date'] == date]
    del df['date']
    return date_dict

def get_tweets_by_location(df):
    """
    Input - Tweets DF with location
    Returns - Dict with location as key and tweets
              as the value
    """
    locations = pd.unique(df.finallocation)

    location_dict = {}

    for location in locations:
        location_dict[location] = df[df['finallocation'] == location]
    
    return location_dict