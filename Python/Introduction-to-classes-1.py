# Let's create a class that will contain an Invoice. Then you will need to create a function that allow you to create the invoice. In other words, the invoice that will contain a self, client, and total.

class Invoice:
  
  # __init__ will give the ability to the function to called later on...

  def __init__(self, client, total):
    self.client = client
    self.total = total
# We need to create another function that will help us to maintain a fromatt. 

  def formatter(self):
    return f'{self.client} owes: ${self.total}'

# Create the variable and call the class with the name of your client and how much the own.

vivint = Invoice('Vivint', 100)
disney = Invoice('Disney', 200)

# Print the value and don't forget to use the variable and the function.

print(vivint.formatter())
print(disney.formatter())