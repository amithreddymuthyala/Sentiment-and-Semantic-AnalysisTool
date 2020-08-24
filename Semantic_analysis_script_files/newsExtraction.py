from newsapi import NewsApiClient
import csv
import re


# Define a function to clean tweets step by step
def clean(raw_str):
    # Handling exception case
    if raw_str is None:
        return raw_str

    # For removing urls
    string = re.sub(r'https\S+', '', raw_str, flags=re.MULTILINE)
    # string = re.sub(r'[^\x00-\x7F]+|http\S+', '', raw_str)

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


# Create first row with column headers
with open("news.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["author", "title", "description", "content"])


# Create connection and add rows
def news(keyword):
    # Connection api
    api = NewsApiClient(api_key='c8818b3b934645baa440e57715c3cee8')
    news_articles = api.get_everything(q=keyword, language='en', sort_by='popularity', page_size=100)

    # Consider each line in articles
    for line in news_articles["articles"]:
        # Open file and write rows
        with open("news.csv", "a", newline='') as cs_file:
            cs_writer = csv.writer(cs_file)
            cs_writer.writerow(
                [clean(line["author"]), clean(line["title"]), clean(line["description"]), clean(line["content"])])


# Get Data with these search keywords
news("Canada")
news("University")
news("Dalhousie University")
news("Halifax")
news("Canada Education")
