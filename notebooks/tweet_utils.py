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
        if (pd.isna(curr_row['full_text'])) or pd.isna(curr_row['created_at']) or not str(curr_row['created_at']).endswith("2019"):
            rows_to_drop.append(i)
        elif curr_row['lang'] == '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>':
            rows_to_drop.append(i)
    print ("Dropping", len(rows_to_drop), "rows!")
    if len(rows_to_drop) == 0:
        return df
    return df.drop(rows_to_drop)


def get_sentiment(df):
    """
    Input - A dataframe of tweets from the CSV file.
    Returns - A dict mapping tweetid to sentiment.
    """
    vader = SentimentIntensityAnalyzer()
    
    tweets = df['full_text']
    tweet_ids = [str(int(x)) for x in df['id']]
    
    sentiment_dict = {}

    for i, tweet in enumerate(tweets):
        sentiment_dict[tweet_ids[i]] = vader(tweet)
    
    return sentiment_dict


def tweets_by_day(df):
    """
    Input - A df with created_at column
           converted by pd.to_datetime
    Returns - A dict with date as key and
             tweets on that date as values
    """
    min_date = min(df['created_at']).date()
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