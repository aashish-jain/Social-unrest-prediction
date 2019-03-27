from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_glove_dict(glove_path="../../glove_vectors/glove.6B.300d.txt"):
    """
    Input - Path to GLoVe txt file, default=300D txt file
    Returns - Dict below

    Create a dict with word as key and word vector as value
    """
    d = {}
    f = open("../../glove_vectors/glove.6B.300d.txt", 'r')
    for row in f:
        row = row.replace('\n', '').split(" ")
        word = row[0]
        vector = np.array([float(x) for x in row[1:]])
        d[word] = vector
    f.close()
    return d

def generate_labels(num_events, lead_days=2, days_window=2):
    """
    Input -
        num_events - as generated as above
        lead_days - the number of days to after which we
                   look for the occurence of an event.
                   Basically, the future
        day_window - If an event occurs in a window of days
                     after num_days

    Returns - Returns labels generated as below

    Generate labels by using the future events, basically
    look-ahead to create labels. If an event occurs from
    i to i + num_days, then label is 1.0 else 0.0
    
    TODO - Maybe implement this with np.stride_tricks?
    """
    n = len(num_events)
    labels = np.zeros(n - lead_days - days_window)
    for i in range(n - lead_days - days_window):
        labels[i] = 1.0 if sum(num_events[i + lead_days: i + lead_days + days_window] > 0) else 0.0
    return labels

def get_cities(df, top_locations):
    """
    Input - DF from reading ACLED CSV
    Returns - String of cities requested based on
              top_locations in process_acled_csv(..)
    """
    counter = Counter(df.location)
    if top_locations == -1:
        return list(counter.keys())
    counter = sorted(counter.items(), key=lambda x: -x[1])[:top_locations]
    return [x[0] for x in counter]


def process_acled_csv(path_to_csv, top_locations=10, lead_days=2, days_window=5, start=None, end=None):
    """
    Input -
        path_to_csv - The path to the CSV file and returns labels
        top_locations - Number of top cities that generated ACLED articles
                        if top_locations is -1, returns for all cities
                        Default value = 10
        lead_days - Lead days before which a prediction should be made
        days_window - The number of days after lead_days that we are
                      concerned about
        start - Start date from which data is needed [Inclusive]
        end - End date to which data is needed [Also inclusive]
    Returns - Labels for each location and each of the dates in the CSV
    """
    # Read file
    try:
        df = pd.read_csv(path_to_csv)
    except:
        raise FileNotFoundError

    df['event_date'] = pd.to_datetime(df['event_date'])
    df.sort_values(by=['event_date'], inplace=True)

    # As the data is sorted, we can do this:
    if start is None:
        start = pd.iloc[0]["event_date"]
    if end is None:
        start = pd.iloc[-1]["event_date"]

    # Convert to DateTime object
    if isinstance(start, str):
        start = pd.to_datetime(start)

    if isinstance(end, str):    
        end = pd.to_datetime(end)

    df = df[df['event_date'] >= start]
    df = df[df['event_date'] <= end]

    # Generate date range for creating labels
    dates = pd.date_range(start=start, end=end)
    print("Data from", start, "to", end, " & Number of days -", len(dates))

    # Get names of cities
    cities_to_process = get_cities(df, top_locations)

    # Dict to map cities to labels
    label_dict = {}

    # Generate number of events, labels and add to
    # mapping
    for city in cities_to_process:
        city_df = df[df["location"] == city]
        num_events = np.zeros(len(dates))
        for i, date in enumerate(dates):
            num_events[i] += len(city_df[city_df['event_date'] == date])
        labels = generate_labels(num_events, lead_days, days_window)
        label_dict[city] = labels
    
    return label_dict


def plot_counter(arr, num_elements=10, reverse=True, xlabel="", ylabel="", title=""):
    """
    Input -
        arr - This could be an list/np.ndarray/pd.Series etc
        num_elements - Number of elements needed to be plotted,
                       default value = 10
        reverse - The ordering for Counter elements, defaule value
                  = True
        xlabel, ylabel, title - plt params
    Returns - Plot the bar graph accordingly

    Probably the most useful function.
    """
    # Get counter
    counter = Counter(arr)

    # Sort as per criterion given in function definition
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=reverse)[:num_elements]

    counter = np.array(counter)

    things , counts = counter[:, 0].tolist(), counter[:, 1].astype(np.float32)
    indices = np.arange(len(counts))
    width = 1


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(indices, things)
    plt.title(title)

    plt.rcParams['figure.figsize'] = (20, 10)
    _ = plt.bar(indices, counts, 0.5)
