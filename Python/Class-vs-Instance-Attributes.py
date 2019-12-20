# Class vs Instance


# We will need to think that a class is a Human or Person that will have some variables like something unique that is attached to them like their carrer, hair color, eye colors, etc. 

# If you have two different persons, you will need to think that every individual it's an instance.



class Persons:
  def __init__ (self,name,profession):
    self.name = name
    self.profession = profession
    self.skills = []

  def addskills (self, skill):
    self.skills.append(skill)

p1 = Persons('Andres', 'Engineer')
p2 = Persons('Mathew', 'Software Developer')

print(p1.name + ' is an ' + p1.profession)
print(p2.name)

p1.addskills('Solve math problems')
p1.addskills('Coding & Design')
p2.addskills('Writting and Reading')

print (p1.skills)