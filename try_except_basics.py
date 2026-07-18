# try/except basics

try:
  with open('missing.csv', 'r') as f:
    print(f.read())

except FileNotFoundError:
  print('File not found!')

