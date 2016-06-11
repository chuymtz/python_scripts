# How to access an element in a list.

animals = ['bear', 'tiger', 'penguin', 'zebra']
# bear = animals[0]

print "If the code is right, then I only print True statements"
print "bear" == animals[0]
print "tiger" == animals[1]
print "penguin" == animals[2]
print "zebra" == animals[3]

print "."*10, "\n"

# Take this list of animals, and follow the exercises where I tell you to write down what animal you get for that ordinal or cardinal number. Remember if I say "first", "second", then I'm using ordinal, so subtract 1. If I give you cardinal (like "The animal at 1"), then use it directly.

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "First I print the list:"

for i in animals:
    print i

print "."*10, "\n"

print "The animal at 1", animals[1]
print "The thid (3rd) animal", animals[2]
print "The first (1st) animal", animals[0]
print "The animal at 3", animals[3]
print "The fifth (5th) animal", animals[4]
print "The animal at 2", animals[2]
print "The sixth (6th) animal", animals[5]
print "The animal at 4", animals[4]
