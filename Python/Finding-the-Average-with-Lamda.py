# This is the code if we use lambda
# We need to use the reduce() function. 

from function import reduce

def Average (lst):
  return reduce (lambda a,b: a + b, lst) / len (lst)

# Driver code

lst = [10,9,100,150,85,35,57,99]
average = Average(lst)

# Printing the Aevrage of the list

print ("This is the Average =", round(round, 2))