import warnings
import numpy as np

from tabulate import tabulate
from collections import Counter
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
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
    # Vader
    vader = SentimentIntensityAnalyzer()

    # Create & populating dict mapping document_id
    # to sentiment dict
    sentiment_dict = {}

    for i, document in enumerate(documents):
        if document_ids[i] not in sentiment_dict:
            sentiment_dict[document_ids[i]] = vader.polarity_scores(document)

    return sentiment_dict


def make_predictions(location_features_dict, labels, model=None, permute=False, lead_days=2, days_window=5):
    """
    Input - 
            location_features_dict - The dict mapping from location to features
            labels - Label dict generated from process_acled_csv(..)
            model - Specific sklearn model to evaluate/benchmark performance
            permute - Permute the data before train-test split
    Returns - None
    """
    # Table for presenting on tabulate
    result_table = []

    # Suppress warnings for divide-by-zero error
    warnings.filterwarnings("ignore")

    # Compute intersection for locations present on both dicts
    common_locations = set(location_features_dict.keys()) & set(labels.keys())

    # Sorted for clarity
    common_locations = sorted(list(common_locations))

    for common_location in common_locations:
        # Get data and labels
        X, y = location_features_dict[common_location], labels[common_location]
        X, y = np.array(X), np.array(y)

        # Eliminate last days to match labels.shape
        X = X[:-(lead_days + days_window)]

        # Permute randomly if specified
        if permute:
            p = np.random.permutation(len(X))
            X, y = X[p], y[p]

        # Split data into train & test - 75% & 25%
        split = int(0.75 * len(X))
        xtrain, ytrain = X[:split], y[:split]
        xtest, ytest = X[split:], y[split:]

        # Default model
        if model is None:
            model = xgboost.XGBClassifier(n_estimators=200, n_jobs=-1)

        # Fit the train data
        model.fit(xtrain, ytrain)

        # Make predictions
        ypred = model.predict(xtest)

        # Compute metrics
        train_acc = model.score(xtrain, ytrain)
        test_acc = model.score(xtest, ytest)
        precision = precision_score(ytest, ypred)
        recall = recall_score(ytest, ypred)
        f1 = f1_score(ytest, ypred)

        # Add row to result_table
        result_row = [
                      common_location,
                      np.round(train_acc, 2), np.round(test_acc, 2),
                      np.round(precision, 2), np.round(recall, 2),
                      np.round(f1, 2), np.round(np.sum(y) / len(y), 2)
                     ]
                      
        result_table.append(result_row)

    # Average stats
    # Turns out median is kind of useless
    result_table_copy = (np.array(result_table)[:, 1:]).astype(np.float32)
    averages = np.round(np.mean(result_table_copy, axis=0), 2)
    
    # Sort by test accuracy
    result_table = sorted(result_table, key=lambda x: -x[-2])


    # Add them to the existing result table
    result_table.append(["Average"] + averages.tolist())

    # Header for table
    header = ["Location", "Train Accuracy", "Test Accuracy",
              "Precision", "Recall", "F1 Score", "+'s in data"]
    
    # Print tabulated result
    print(tabulate(result_table, 
                   tablefmt="pipe", 
                   stralign="center", 
                   headers=header))
    
    # Unsuppress warning
    warnings.filterwarnings("default")
    return

def get_features(date_dict):
    """
    Input: date_dict to compute features for each date
    Returns: Features for each date
    """
    # Initialize list for features
    features = []

    # Iterate through dates
    for date in date_dict:
        feature_row = []
        docs = date_dict[date]

        # If no rows are present, add zero-row
        if docs is None:
            feature_row = [0] * 6
        else:
            # Compute features
            feature_row.append(len(docs))
            mean = docs.mean()

            feature_row.extend(
                [mean['pos'], mean['neg'], mean['neu'], mean['compound']])
            feature_row.append(len(docs[docs['neg'] > 0]))

        # Add feature_row to above list
        features.append(feature_row)
    return features
