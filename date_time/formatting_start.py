# 
# How to format time and date output
#

from datetime import datetime

def main():
	# times and dates can be formateed using a set of predefined string
	# control codes
	now = datetime.now()
	
	# Date formatting

	# some codes to know
	# %y or Y give year
	# %a or A give weekday
	# %b or B give month
	# %d  give day of month
	print now.strftime("%Y")
	print now.strftime("%y")
	print now.strftime("%a, %d, %B, %y")

if __name__  == "__main__":
	main();
