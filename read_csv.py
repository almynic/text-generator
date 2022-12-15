import csv

with open('data/variations.csv', newline='', encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    # you may also want to remove whitespace characters like `\n` at the end of each line
    for row in reader:
        headers = reader.fieldnames
        for h in headers:
            print(row[h])
            
            
