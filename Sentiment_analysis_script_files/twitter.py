import csv
import tweepy
import re

# Credentials
consumer_key = "PzMSqjD8Xm3X9ZecsYxbI0zek"
consumer_secret = "il3VOuJ5b5G3ae01XpJHnGHP50gB7wIKm77icBkMgO7wk38a9B"
access_key = "1233476346405367810-q8OoTJa7JfSvxou2P5hB0KQOXfkZvR"
access_secret = "kbRMp6tEsBUmz5wpG97c9Qpq6PcRpMiFHLom9xWNNTMf2"


# Define a function to clean tweets step by step
def clean(str):
    # For removing urls
    string = re.sub(r'https\S+', ' ', str, flags=re.MULTILINE)

    # For removing emoticons
    string = [i.encode('ascii', 'ignore').decode('ascii')
              for i in string.split(" ")]

    # Join the cleaned words in a list
    string = " ".join(string)

    # For removing unwanted hashtags
    string = re.sub(r'#\w+ ?', ' ', string, flags=re.MULTILINE)

    # Remove unnecessary characters
    string = [re.sub(r"[^a-zA-Z0-9]+", ' ', j)
              for j in string.split(" ")]

    # Join the cleaned words in a list
    string = " ".join(string)

    # Return the string
    return string


# With tweets csv file open
with open("tweets.csv", "a", newline='') as csv_file:
    # Create a csv writer object
    csv_writer = csv.writer(csv_file)
    # Create first default row with column names for csv file
    csv_writer.writerow(["Tweet", "Time", "Location", "RT"])

# Make a call to API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Set wait_on_rate_limit to hit multiple times
api = tweepy.API(auth, wait_on_rate_limit=True)

# Extract tweets from twitter
tweets = tweepy.Cursor(api.search,
                       q="Canada OR University OR Dalhousie University OR Halifax OR Canada Education").items(3100)

# Enter next rows in the csv file
for line in tweets:
    # With tweets csv file open
    with open("tweets.csv", "a", newline='', encoding="utf-8-sig") as csv_file:
        # Create a writer object
        csv_writer = csv.writer(csv_file)

        # Perform cleaning on these attributes and append those rows to the file
        csv_writer.writerow([clean(line._json["text"]), clean(line._json["created_at"]), line._json["user"]["location"],
                             line._json["retweet_count"]])
