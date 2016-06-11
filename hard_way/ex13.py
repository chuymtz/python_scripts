from sys import argv # This is the "import" line

script, first, second, third = argv # argument variable

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# when you execute, write 
#		python ex13.py first 2nd 3rd
# so that python assigns script = ex13.py, first = first, second = 2nd etc
# After this you can use these variables.

x = raw_input("What is the name of your script?")

print "The name of the script is %r" % x 
