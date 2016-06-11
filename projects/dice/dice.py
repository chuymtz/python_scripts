#from random import randint
import random

def roll_dice(n):
	random_number = random.randint(1,6)
	print("\nYou have rolled a {}.\n".format(random_number))
	main_menu()

def dice_menu():
	print('\nEnter the number of dice.\n')
	num_dice = int(input('> '))
	roll_dice(num_dice)


def main_menu():
	print('Type \'q\' to quit.')
	print('Type \'n\' to select the number of dice.\n')
	ans = input('> ')
	
	check = True
	while check == True:
		if ans == 'q':
			#check = False
			quit()
		elif ans == 'n':
			dice_menu()
		else:
			main_menu()
		


def main():
	print('\n Welcome to my 1st Dice Similator!\n')
	main_menu()


if __name__ == "__main__": main()
