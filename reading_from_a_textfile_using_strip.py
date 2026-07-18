# Reading from a text file using .strip command (line by line)

with open ('file.txt', 'r')  as f:
  for line in f:
    print(line.strip())

