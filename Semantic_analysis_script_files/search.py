import re
import csv
import math

searchWords = ["Canada", "University", "Dalhousie University", "Halifax", "Business"]

# Create first row with column headers
with open("table1.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Total Documents", "500"])
    csv_writer.writerow(
        ["Search Query", "Document containing term(df)", "Total Documents(N)/ number of documents term appeared(df)",
         "Log10(N/df)"])

for word in searchWords:
    # Open news and get number of rows
    with open("news.csv", "r", encoding='utf-8-sig') as csv_file:

        # Get count of number of rows
        reader1 = csv.reader(csv_file, delimiter=',')
        data = list(reader1)

        # Exclude header line
        n = len(data) - 1

        c = 1
        count = 0

        # Search for keyword in each file
        for files in range(0, n):
            flag = 0
            name = "file"
            name = name + str(c) + ".csv"
            stringFound = re.findall(r'\b%s\b' % word, open(name).read())
            if stringFound:
                flag = 1
            if flag == 1:
                count = count + 1
            c = c + 1
        # print(count)
    with open("table1.csv", "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([word, count, round((n / count), 2), round(math.log10(n / count), 2)])
