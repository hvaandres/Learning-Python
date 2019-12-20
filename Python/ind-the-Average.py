# Finding the Average of a lis of 8 digits by using Sum

def Average(lst):
  return sum(lst) / len(lst)

# Driver code

lst = [10,9,100,150,85,35,57,99]
average = Average(lst)

# Printing Average of the list

print ("This is the Average =", round(average, 2))


