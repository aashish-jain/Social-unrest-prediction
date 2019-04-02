import pandas as pd

from .nlp_utils import get_sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def clean_df(df):
    """
    Input - A df of tweets
    Returns - A df that cleans the input 
             df and returns it
    TODO - Vectorize this
    """
    # Indices for rows_to_drop
    rows_to_drop = []

    for i in range(len(df)):
        # Current row of data
        curr_row = df.iloc[i]
        
        # Drop row without TweetID
        if pd.isna(curr_row['id']):
            rows_to_drop.append(i)
        
        # Drop row without text/timestamp
        if (pd.isna(curr_row['full_text'])) or pd.isna(curr_row['created_at']):
            rows_to_drop.append(i)
        
        # Handle timestamp as str or pandas TimeStamp
        # Drop row if tweet not created in 2019
        if isinstance(curr_row['created_at'], pd._libs.tslibs.timestamps.Timestamp):
            if curr_row['created_at'].year != 2019:
                rows_to_drop.append(i)

        elif isinstance(curr_row['created_at'], str):
            if "2019" not in curr_row['created_at']:
                rows_to_drop.append(i)
            
        # Abnormal lanuage case [Maybe unnecessary]
        if curr_row['lang'] == '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>':
            rows_to_drop.append(i)

    print ("Dropping", len(rows_to_drop), "rows!")

    # If nothing to drop, return df as such
    if len(rows_to_drop) == 0:
        return df

    # Drop invalid rows
    return df.drop(rows_to_drop)

def add_sentiment_to_df(df, doc_ids, sentiment_dict):
    """
    Input - 
            df - Dataframe passed by get_[tweet/headlines]_sentiment
            doc_ids - UUID for docs
            sentiment_dict - Dict mapping doc_ids to sentiment dict
    Returns - DF with sentiment columns
    """

    # Initialize lists for each polarity
    neg, pos, neu, compound = [], [], [], []

    # Populated above lists
    for i in range(len(df)):
        row = df.iloc[i]
        sentiment = sentiment_dict[doc_ids[i]]
        neg.append(sentiment['neg'])
        pos.append(sentiment['pos'])
        neu.append(sentiment['neu'])
        compound.append(sentiment['compound'])
    
    # Add to DF
    df['neg'] = neg
    df['neu'] = neu
    df['pos'] = pos
    df['compound'] = compound

    return df


def get_tweet_sentiment(df):
    """
    Input - A dataframe of docs from the CSV file
    Returns - A df with extra sentiment columns

    This is a driver function handles tweets
    """
    # Get docs and doc_ids
    tweets = df['full_text']
    tweet_ids = [str(int(x)) for x in df['id']]
    
    # Get sentiment mapping
    sentiment_dict = get_sentiment(tweets, tweet_ids)
    
    # Add sentiment to DF
    df = add_sentiment_to_df(df, tweet_ids, sentiment_dict)

    return df

def get_headlines_sentiment(df):
    """
    Input - A dataframe of docs from the CSV file
    Returns - A df with extra sentiment columns

    This is a driver function handles headlines
    """
    # Get docs and doc_ids
    docs = df['headline_text']
    doc_ids = range(len(df))
        
    # Get sentiment mapping    
    sentiment_dict = get_sentiment(docs, doc_ids)

    # Add sentiment to DF
    df = add_sentiment_to_df(df, doc_ids, sentiment_dict)

    return df



def get_docs_by_day(df, min_date=None, max_date=None):
    """
    Input - A df with created_at column
           converted by pd.to_datetime
    Returns - A dict with date as key and
             tweets on that date as values
    """
    # Generate start and end dates if necessary
    if min_date is None:
        min_date = min(df['created_at']).date()
    
    if max_date is None:
        max_date = max(df['created_at']).date()
    
    # Initialize dict
    date_dict = {}
    
    # Sanity check
    assert(max_date > min_date)
    
    # Generate date range
    date_range = pd.date_range(min_date, max_date)
    
    # Generate dates for timestamps
    dates = [x.date() for x in df['created_at']]
    
    df['date'] = dates
    
    # Iterate through dates
    for date in date_range:
        # Get documents for the day
        docs = df[df['date'] == date.date()]
        
        # If no docs found, set to None 
        # Else set to docs
        if len(docs) == 0:
            date_dict[str(date)] = None
        else:
            date_dict[str(date)] = docs

    # Drop this column
    del df['date']

    return date_dict


def get_docs_by_location(df):
    """
    Input - Documents DF with location
    Returns - Dict with location as key and tweets
              as the value
    """
    # Get unique locations
    locations = pd.unique(df.finallocation)

    # Initialize dict
    location_dict = {}

    # Iterate through locations and add rows
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
    # Sanity check
    assert(start_date < end_date)
    
    # Get location mapping
    location_dict = get_docs_by_location(df)

    # Initialize 2 level mapping
    location_date_dict = {}

    # Iterate through location
    for location in location_dict.keys():
        # Get docs for each date
        date_dict = get_docs_by_day(location_dict[location], start_date, end_date)

        # Set 2-level mapping
        location_date_dict[location] = date_dict

    return location_date_dict
