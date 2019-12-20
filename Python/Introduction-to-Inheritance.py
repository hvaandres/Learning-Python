# Inheritance: Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class.

class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):
    return f'Hello {self.first_name} {self.last_name}'


# This is a child class
class AdminUser(User):
  def active_users(self):
    return '1000'

# Create a User and insert the child class with their respectively information
Andres = AdminUser('aharo@foxie.com', 'Andres', 'Haro')

Crisitna = User('charo@foxie.com', 'Cristina', 'Haro')

# Print the values
print(Andres.active_users())
print(Andres.greeting())

# This will print an error since we don't have a way to see the child class.
print(Crisitna.active_users())