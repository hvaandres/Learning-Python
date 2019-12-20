# Polymorphism: In literal sense, Polymorphism means the ability to take various forms. In Python, Polymorphism allows us to define methods in the child class with the same name as defined in their parent class. ... In such cases, you will have to re-implement method in the child class.



# Parent class

class Html:
  def __init__(self, content):
    self.content = content

# Abstract Function - Holding and sharing behaviour. All the child classes will be aable to call the parent.

  def render(self):
    raise NotImplementedError('Subclass must implement render method')

class Heading(Html):
  def render(self):
    return f'<h1>{self.content}</h1>'

class Div(Html):
  def render(self):
    return f'<div>{self.content}</div>'

tags = [
        Div('First Div'),
        Heading('My firsts Heading'),
        Div('Second Div')
        ]

for tag in tags:
  print(tag.render())
