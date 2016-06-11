#
# HOW TO MANIPULATE TIMES AND DATES IN PYTHON
#


from datetime import date
from datetime import time
from datetime import datetime

def main():
	## Date objects
	# Get todays date from simple today() method in date class
	today = date.today()
	print "\nToday's date is ", today

	# print out the date's indivual components
	print "\nToday's day is ", today.day
	print "\nToday's month is ", today.month
	print "\nToday's year is ", today. year

	# retrieve today's weekday number
	print "\nToday's weekday # is ", today.weekday()

	# NOW USE DATETIME TO GET TIMES
	today_time = datetime.now()
	print "\nThe current date and time is ", today_time

	#Get current time
	t = datetime.time(datetime.now())
	print "\nThe current time is ", t

	# weekday return the number of the weekday
	wd = date.weekday(date.today())
	# once you have the number use that index to access the correct word from the following list
	days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunda"]
	print "\nToday is day number %d" % wd
	print "which is a ", days[wd]

if __name__ == "__main__":
	main();
