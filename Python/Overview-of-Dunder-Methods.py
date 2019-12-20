

# Overview of Dunder Methods

class Invoice: 
  def __str__(self):
    return "This is the Invoice Class!"

inv = Invoice()
print(str(inv))

class Invoice:
  def __init__(self,client, total):
    self.client = client
    self.total = total

  # The string will help me to test my code and see if it will print my data correctly or not. In other words, will provide you the values and the details with our class.
  
  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

inv = Invoice('Disney', 1000)
print(str(inv))