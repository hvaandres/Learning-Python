#For Loop is when you know when you will need to Stop

#While Loop you will need to let the program when to stop because the while loop will never stop. Unless you set up an specific value.

"""
nums = list(range(1,100))

while len(nums) > 0:
  print(nums.pop())
"""

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()


