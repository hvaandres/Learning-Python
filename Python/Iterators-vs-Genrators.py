class UnfinishedBrand:
    def __init__(self, cars):
        self.cars = cars

    def lineup(self):
        lineup_max = len(self.cars)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.cars[idx]
            else:
                idx = 0
                yield self.cars[idx]

            idx += 1

    def __repr__(self):
        return f'UnfinishedBrand({self.cars})'

    def __str__(self):
        return f"UnfinishedBrand with the cars: {', '.join(self.cars)}"


brands = [
  'Nissan',
  'Ford',
  'Chevrolet',
  'Mercedez',
  'BMW',
  'Alfa Romeo',
  'Toyota',
  'Lambo',
  'Masseretti'
]

full_brand = UnfinishedBrand(brands)
car_list = full_brand.lineup()

print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))
print(next(car_list))



print(repr(full_brand))

print(str(full_brand))