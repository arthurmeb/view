import csv
import json

# list to hold the data from each CSV file
files = ["Eminem.csv", "Immortal Technique.csv", "Joey Bada$$.csv", "J. Cole.csv"]
data = []

# open and read each CSV file
for i in files:
    name = i.replace('.csv', '')
    with open(f"{name}.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # write the data to a JSON file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

    # read the JSON file
    with open('data.json') as json_file:
        data = json.load(json_file)

    # write the data to a CSV file
    fieldnames = data[0].keys()
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
