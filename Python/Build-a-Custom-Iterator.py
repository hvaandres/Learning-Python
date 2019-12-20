# Building a Custom Iterator

class Brands:
  def __init__(self, cars):
    self.cars = cars
  # We will need to use -1 to make sure our car list will start from 0 to 8.
    self.last_cars_index = (len(self.cars)-1)
  
  # If you adjust the self.n=0 will allow you to start from the brand that you want. Exaample if you insert 1, this one will start from Nissan instead of Ford.

  def __iter__(self):
    self.n=0
    return self

  def get_cars(self, n):
    return self.cars[n]
  
  # If you adjust the self.n number will allow you to get a list with certain brand of car. You can select the start and the end!

  def __next__(self):
    if self.n < self.last_cars_index:
      carro = self.get_cars(self.n)
      self.n +=1
      return carro
    elif self.n == self.last_cars_index:
      carro = self.get_cars(self.n)
      self.n = 0
      return carro



car = [
  'Ford',
  'Nissan',
  'Aston Martin',
  'BMW',
  'Audi',
  'Mercedez Benz',
  'Porsche',
  'Jeep',
  'Mini'
]

car_brand = Brands(car)
process = iter(car_brand)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))