
# Dunder Methods (__repr__)


class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f"Invoice( client: {self.client}, Total: {self.total})"


inv = Invoice('Disney', 1500)
print(str(inv))
print(repr(inv))