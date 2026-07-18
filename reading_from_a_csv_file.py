# Reading from a csv file

import csv

with open ('student.csv', 'r', newline = '') as f:
  reader = csv.reader(f)

  for row in reader:
    print(row)

