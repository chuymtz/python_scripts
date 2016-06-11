# Now we learn to read from a file.

# this line is the usual argv stuff
from sys import argv


# assign script and filename to the variables you intput at the begginging
script, filename = argv
prompt = '>>> ' # assign the string prompt to the var prompt


# this open the file filename and stores it in txt to later use
txt = open(filename) 

# here we tell the user the name of the file and then use command read to display
print "Here's your file %r:" % filename
print txt.read()

# this is just another way of doing this without the argv method
print "Type the filename again:"
file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()

# Try to close the file. This frees up space.
txt.close()
txt_again.close()
