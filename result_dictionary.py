students = [
    {'name' : 'Sara', 'age' : 15, 'passed' : True},
    {'name' : 'Ali', 'age' : 10, 'passed' : False},
    {'name' : 'Hiba', 'age' : 20, 'passed' : True}
]
for s in students:
  print(f'{s['name']} aged {s['age']} is passed.')
