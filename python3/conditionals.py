

a, b = 5, 1

if a < b:
	print("a ({}) is less than b ({})". format(a, b))
else:
	print("a ({}) is not less than b ({})". format(a, b))


print('foo' if a < b else 'bar')
# does the old method work?

#print "The values of a is %d" % a

#it turns out the above script doesnt work well
#on python 3
