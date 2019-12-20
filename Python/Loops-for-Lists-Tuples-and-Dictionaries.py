"""

# The best way is creating a list

schools = ['UVU','The U','BYU','Guadalajara']

# School = Individual
# Schools = The List of the schools
# The for loop will allows us to see every item from the list
# note: You can use a tuple schools = ('UVU','The U','BYU','Guadalajara') & everything will be the same....

for school in schools:
  print(school)

"""
# Key value dictionary
schools = {
  'UVU':'Utah Valley University',
  'The U':'The University of Utah',
  'SLCC':'Salt Lake City Community College',
  'BYU':'Brigham Young University'
}

# We need to grab the Key & Value
# Position is the key like: UVU, The U, ETC.
# School is the full name from the school
for position, school in schools.items():
  print('Abrebiation', position)
  print('School Names', school)

# Identation is very important with loops in python because without the print you will not be able to move forward
 