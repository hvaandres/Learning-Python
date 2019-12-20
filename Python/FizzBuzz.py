"""
Write a program that prints the numbers from 1 to 100. Where multiples of three will print "Fizz" and multiples of five will print "Buzz". Also, multipple of thrre and five together will print "FizzBuzz"

"""

def fizz_buzz(max_num):
  for num in range(1, max_num +1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)

fizz_buzz(100)