import csv
import re
import collections

with open("visualization2.csv", "a", newline='', encoding="utf-8-sig") as csv_file:
    # Create a csv writer object
    csv_writer = csv.writer(csv_file)
    # Create first default row with column names for csv file
    csv_writer.writerow(["Tweet_id", "match_word", "match_word_count", "word_polarity"])


def sentiment(str):
    # With tweets csv file open
    with open("visualization2.csv", "a", newline='', encoding="utf-8-sig") as csv_file:

        # Create a writer object
        csv_writer = csv.writer(csv_file)

        # To get bag of words
        bagofwords = [collections.Counter(re.findall(r'\w+', txt)) for txt in str]

        positivewords = re.findall(r'\b\S+\b', open('positive-words.txt').read())
        negativewords = re.findall(r'\b\S+\b', open('negative-words.txt').read())

        # Traverse through bag of words one by one
        for i in range(0, len(str)):
            sum = 0
            # Check for positive words in bag-of-words
            for word in positivewords:
                sum = sum + bagofwords[i][word]
                if bagofwords[i][word] > 0:
                    csv_writer.writerow([i + 1, word, bagofwords[i][word], "positive"])
            # Check for negative words in bag-of words
            for word in negativewords:
                sum = sum - bagofwords[i][word]
                if bagofwords[i][word] > 0:
                    csv_writer.writerow([i + 1, word, bagofwords[i][word], "negative"])


# Define a function to clean tweets step by step
def clean(str):
    # Remove unnecessary characters
    string = [re.sub(r"[^a-zA-Z]+", ' ', j)
              for j in str.split(" ")]

    # Join the cleaned words in a list
    string = " ".join(string)

    # Remove RT from tweet
    string = re.sub(r'RT', '', string, flags=re.MULTILINE)

    # Return the string
    return string


# Enter each new tweet into a list
myline = []
with open("noduplicatetweetscsv.csv", "r", encoding='utf-8-sig') as csv_file:
    # Create a csv reader object
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        myline.append(clean(line["Tweet"]).lower())

# Call sentiment function
sentiment(myline)
