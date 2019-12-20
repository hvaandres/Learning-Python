def price (price, addition):
  if isinstance(addition, int):
    addition = addition * 0.08
  return int(price) + addition

print(price(5.20, 99))
print(price(5.90, 1.20))
print(price(4, 60))
print(price(6, 50))
print(price(8, 99))
print(price(3, 2))