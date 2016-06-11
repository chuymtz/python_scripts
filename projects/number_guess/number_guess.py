import random

def play_again_question():
	print('Would you like to play again? Yes or No?\n')
	while True:
		again = input('> ')
		if again == 'No':
			quit()
		elif again == 'Yes':
			choose_range()
		else:
			print('Tell me either "Yes" or "No".')

def guess_num(a, b, n):
	print('\nI have produced a number x in the interval [{},{}]! You have {} guesses!\n'.format(a, b, n))
	x = random.randint(a,b)
	check = True
	tries = 1
	while check == True:
		ans = int(input('x = '))
		tries += 1
		if ans == x:
			print('\nYou guessed correctly!\n')
			check = False
		elif tries > n:
			print("\nYou've ran out of chances! The answer was {}\n".format(x))
			play_again_question()
		elif ans < x:
			print('\nYou guessed too low\n')
		elif ans > x:
			print('\nYou guessed too high\n')
	play_again_question()	
	
def choose_range():
	print('How many chances to guess?\n')
	n = int(input('n = '))
	print('\nChoose a range (a,b) to choose x from.\n')
	a = int(input('a = '))
	b = int(input('b = '))
	#print('\nYou have chosen {} and {}.'.format(a,b)+'\n')
	guess_num(a, b, n)	

def main():
	print('''
		This program generates a random 
		integer x between a and b inclusive 
		and gives you n chances to
		guess it.\n
		''')
	choose_range()

if __name__ == "__main__": main()
