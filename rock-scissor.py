#Make a two-player Rock-Paper-Scissors game

import sys

player1 = input("Enter name for player1")
player2 = input("Enter name for player2")

player1_choice = input("%s, do yo want to choose rock, paper or scissors?" % player1)
player2_choice = input("%s, do yo want to choose rock, paper or scissors?" % player2)

def compare(c1,c2):
	if c1 == c2:
		return('Its a tie')
	elif c1 == 'rock':
		if c2 == 'scissor':
			return("Rock wins")
		else:
			return("Paper wins")
	elif c1 == 'scissor':
		if c2 == 'paper':
			return("Scissor wins")
		else:
			return("Rock wins")
	elif c1 == 'paper':
		if c2 == 'rock':
			return("Paper wins")
		else:
			return("Scissor wins")
	else:
		return("Invalid choice given")
		sys.exit()

print(compare(player1_choice, player2_choice))