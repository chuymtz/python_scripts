from sys import argv #This is the usual sys library and argv book

script, filename = argv # declare two features

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") #awaits confirmation

print "Opening the file..."
target = open(filename, 'w') #what is the 'w' for?

print "Truncating the file. Goodbye!"
target.truncate() #deletes the existing text in the filename file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#message = line1, "\n", line2, "\n", line3, "\n"
#target.write(message)

print "And finally, we close it."
target.close()
