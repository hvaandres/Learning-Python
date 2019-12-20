# Finding the Average Number with mean()

from statistics import mean

def Average(lst):
  return mean(lst)

# Driver Code

lst = [100,86,99,3,33,44,66,77]
average = Average(lst)

# Printing the Average

print("This is the Average =", round(average, 2)) 