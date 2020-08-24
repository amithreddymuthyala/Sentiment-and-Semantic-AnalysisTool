import re
import csv

searchWord = "Canada"

# Create first row with column headers
with open("table2.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Term", "Canada"])
    csv_writer.writerow(["Canada appeared in", "Total words(m)", "Frequency(f)"])

with open("news.csv", "r", encoding='utf-8-sig') as csv_fi:
    # Create a csv reader object
    # csv_reader = csv.DictReader(csv_fi)

    # Get count of number of rows
    reader1 = csv.reader(csv_fi, delimiter=',')
    data = list(reader1)

    # Exclude header line
    n = len(data) - 1

    # Initialize for reading N files
    c = 1
    count = 0

    # Initialize output highest frequency
    outputHighestFreq = 0

    # Initialize output article
    outputArticle = 0
    for files in range(0, n):
        flag = 0
        name = "file"
        name = name + str(c) + ".csv"
        totalWords = re.findall(r'\w+', open(name).read())
        stringFound = re.findall(r'\b%s\b' % searchWord, open(name).read())
        if stringFound:
            # flag = 1
            article = "article #" + str(c)
            with open("table2.csv", "a", newline='') as csv_fil:
                csv_writer = csv.writer(csv_fil)
                csv_writer.writerow([article, len(totalWords), len(stringFound)])

                if len(stringFound) > outputHighestFreq:
                    outputHighestFreq = len(stringFound)
                    outputArticle = "Article #" + str(c)
        c = c + 1
    # Print article with highest frequency
    print(outputArticle + " with Highest frequency: " + str(outputHighestFreq))
