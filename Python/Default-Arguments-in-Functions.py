
# Correct Way

def greeting(name = 'Guest'):
  print(f' Hi {name}!')

greeting()
greeting('haro')

# Big No No (Mitability) This problem will collect the information from the original collection. Memory issue

def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())
