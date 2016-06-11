def main():
	x = (1, 2, 3) # inmutable
	y = [1, 2, 3] # mutable (i prefer this)
	
	y.append(5)
	y.insert(2,7) # insert at position 2 a 7
	
	s = "string" # it is mutable similar to a list

	print(type(x), x, type(y), y, type(s), s)

if __name__ == "__main__": main()
