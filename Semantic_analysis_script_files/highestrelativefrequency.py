import re
import csv

searchWord = "Canada"

with open("news.csv", "r", encoding='utf-8-sig') as csv_fi:
    # Create a csv reader object
    # csv_reader = csv.DictReader(csv_fi)

    # Get count of number of rows
    reader1 = csv.reader(csv_fi, delimiter=',')
    data = list(reader1)

    # Exclude header line
    n = len(data) - 1

    # Create first row with column headers
    with open("table3.csv", "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Term", "Canada"])
        docs = "Canada appeared in " + str(n) + " documents"
        csv_writer.writerow([docs, "Total words(m)", "Frequency(f)", "Relative Frequency(f/m)"])

    # Initialize for reading N files
    c = 1
    count = 0

    # Initialize to find output highest relative frequency
    outputHighest = 0
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
            with open("table3.csv", "a", newline='') as csv_fil:
                csv_writer = csv.writer(csv_fil)
                csv_writer.writerow([article, len(totalWords),
                                     len(stringFound), round(len(stringFound)/len(totalWords), 2)])

                if (len(stringFound) / len(totalWords)) > outputHighest:
                    outputHighest = round(len(stringFound) / len(totalWords), 2)
                    outputArticle = "Article #" + str(c)
        c = c + 1
    # Print article with highest relative frequency
    print(outputArticle + " with Highest Relative frequency: " + str(outputHighest))
