# Short script to process rabbit subreddit data
# C. B. Salling 2015-03-12

import csv


rabbit_data = []
with open('items.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        rabbit_data.append(row)

split_data = []

for row in rabbit_data:
    for word in row:
        split_data.append(word)

for row in split_data:
    print row
