#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != 'exit':
	guess = int(input('Guess a number'))

	if guess == "exit":
		break

	count += 1

	if guess < number:
		print("too Low")
	elif guess > number:
		print("too high")
	else:
		print("Woilaa you guessed it right")
		print("Number of tries were " ,count)