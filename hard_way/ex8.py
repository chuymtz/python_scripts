# Define variable formatter with 4 inputs, decimal or string

formatter = "%r %r %r %r"

# Makes string 1 2 3 4

print formatter % (1, 2, 3, 4)

# same with strings

print formatter % ("one", "two", "three", "four")

# now boolean ops

print formatter % (True, False, False, True)

# I dont know what happens here

print formatter % (formatter, formatter, formatter, formatter)

# Longer strings

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight"
    )	
