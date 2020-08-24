import csv
import re
import collections

with open("sentiment.csv", "a", newline='', encoding="utf-8-sig") as csv_file:
    # Create a csv writer object
    csv_writer = csv.writer(csv_file)
    # Create first default row with column names for csv file
    csv_writer.writerow(["Tweet", "Message", "match", "polarity"])


def sentiment(str):
    # With tweets csv file open
    with open("sentiment.csv", "a", newline='', encoding="utf-8-sig") as csv_file:

        # Create a writer object
        csv_writer = csv.writer(csv_file)

        # To get bag of words
        bagofwords = [collections.Counter(re.findall(r'\w+', txt))
                      for txt in str]

        # Printing bag-of-words for each tweet in a new line
        for i in range(0, len(bagofwords)):
            print(list(bagofwords[i].items()))

        positivewords = re.findall(r'\b\S+\b', open('positive-words.txt').read())
        negativewords = re.findall(r'\b\S+\b', open('negative-words.txt').read())

        # Traverse through bag of words one by one
        for i in range(0, len(str)):
            sum = 0
            text = ""
            # Check for positive words in bag-of-words
            for word in positivewords:
                sum = sum + bagofwords[i][word]
                if bagofwords[i][word] > 0:
                    if text == "":
                        text = word
                    else:
                        text = text + "," + word
                # print(word)
                # print(sum)
            # Check for negative words in bag-of words
            for word in negativewords:
                sum = sum - bagofwords[i][word]
                if bagofwords[i][word] > 0:
                    if text == "":
                        text = word
                    else:
                        text = text + "," + word
            if sum > 0:
                csv_writer.writerow([i + 1, str[i], text, "positive"])
            elif sum < 0:
                csv_writer.writerow([i + 1, str[i], text, "negative"])
            else:
                csv_writer.writerow([i + 1, str[i], text, "neutral"])


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
myLine = []
with open("noduplicatetweetscsv.csv", "r", encoding='utf-8-sig') as csv_file:
    # Create a csv reader object
    csv_reader = csv.DictReader(csv_file)

    # Taking only tweet message
    for line in csv_reader:
        myLine.append(clean(line["Tweet"]).lower())

# Call sentiment function
sentiment(myLine)
