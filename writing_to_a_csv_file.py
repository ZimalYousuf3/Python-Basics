# Writing to a csv file

import csv

with open ('student.csv', 'w', newline = '') as f:
  writer = csv.writer(f)
  writer.writerow(['Name', 'Marks'])
  writer.writerow(['Zimal', 98])
  writer.writerow(['Sara', 78])
  writer.writerow(['Zumar', 82])
  writer.writerow(['Fajar', 94])
  writer.writerow(['Hooria', 86])

print('File written!')

