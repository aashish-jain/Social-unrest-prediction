from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(documents, document_ids):
    """
    Input - A document_df that basically has documents
            and their IDs [tweetid/message hash etc]
    Returns - A dictionary mapping document ID to sentiment
              from Vader

    This function is basically as a function that is generic
    to the documents which at the moment are tweets & news
    articles.
    """


    vader = SentimentIntensityAnalyzer()

    sentiment_dict = {}
    for i, document in enumerate(documents):
        if document_ids[i] not in sentiment_dict:
            sentiment_dict[document_ids[i]] = vader.polarity_scores(document)
    
    return sentiment_dict