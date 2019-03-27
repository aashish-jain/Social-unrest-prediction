import pandas as pd
from nlp_utils import get_sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def clean_df(df):
    """
    Input - A df of tweets
    Returns - A df that cleans the input 
             df and returns it
    TODO - Vectorize this
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


def get_tweet_sentiment(df):
    """
    Input - A dataframe of tweets from the CSV file
    Returns - A df with an extra sentiment column
    TODO - Process only for unique tweets
    """
    tweets = df['full_text']
    tweet_ids = [str(int(x)) for x in df['id']]
    
    sentiment_dict = get_sentiment(tweets, tweet_ids)

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


def get_docs_by_day(df, min_date=None, max_date=None):
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
    
    for date in date_range:
        tweets = df[df['date'] == date.date()]
        
        if len(tweets) == 0:
            date_dict[str(date)] = None
        else:
            date_dict[str(date)] = tweets

    del df['date']
    return date_dict


def get_docs_by_location(df):
    """
    Input - Documents DF with location
    Returns - Dict with location as key and tweets
              as the value
    """
    locations = pd.unique(df.finallocation)

    location_dict = {}

    for location in locations:
        location_dict[location] = df[df['finallocation'] == location]
    
    return location_dict


def interleave_location_and_date(df, start_date, end_date):
    """
    Input - 
            df - A DF with documents
            start_date & end_date - Date maxima

    Returns - A 2-level dict with location as a
              level one key and second level key as 
              dates for feature extraction across 
              the 2 dates
    """
    assert(start_date < end_date)
    
    location_dict = get_docs_by_location(df)
    location_date_dict = {}

    for location in location_dict.keys():
        print(location)
        date_dict = get_docs_by_day(location_dict[location], start_date, end_date)
        location_date_dict[location] = date_dict

    return location_date_dict
