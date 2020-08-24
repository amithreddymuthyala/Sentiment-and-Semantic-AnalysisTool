import re
import csv


def clean(raw_str):
    # Remove unnecessary characters
    string = [re.sub(r"[^a-zA-Z]+", ' ', j)
              for j in raw_str.split(" ")]

    # Join the cleaned words in a list
    string = " ".join(string)

    return string


with open("news.csv", "r", encoding='utf-8-sig') as csv_file:
    # Create a csv reader object
    csv_reader = csv.DictReader(csv_file)
    c = 1
    for line in csv_reader:
        name = "file"
        name = name + str(c) + ".csv"
        # Insert each line in a new file
        with open(name, "a", newline='') as cs_file:
            cs_writer = csv.writer(cs_file)
            cs_writer.writerow(["title", "description", "content"])
            cs_writer.writerow([clean(line["title"]), clean(line["description"]), clean(line["content"])])
        c = c + 1
