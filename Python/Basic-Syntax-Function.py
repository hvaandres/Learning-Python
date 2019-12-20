# Program to log in and print your name and print if you are authorized or not.

def full_name(first, last):
  print(f'{first} {last}')

full_name('andres', 'haro')

def auth(email, password):
  if email == 'aharo@instructure.com' and password == 'chingatumadre':
    print ('You are authorized')

auth('aharo@instructure.com','chingatumadre')


# Will print 100 numbers since you are telling the program to print numbers in between 1, 101. In other words, this function will count from 1 to 100

def hundred ():
  for num in range(1,101):
    print (num)

hundred()

#Dynamic

def counter (max_value):
  for num in range(1, max_value):
    print(num)

counter(10)
