# Nested Dictionaries with the presidents of two different countries....

teams = [
  {
    'USA': {
      'OB': 'Obama',
      'TR': 'Trump',
      'WA': 'Washignton',
    }
  },
  {
    'Mexico': {
      'CA': 'Calderon',
      'PN': 'Pena Nieto',
    }
  }
]

# print(teams[0])

best = teams[1].get('Mexico', 'Team not found')

print(list(best.values())[0])
