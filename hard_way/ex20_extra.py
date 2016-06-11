from sys import argv

script, input_file = argv

file = open(input_file)

print file.readline()

file.seek(0)

print file.readline()

file.close()
