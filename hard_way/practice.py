def int_sum(n):
	stringed_num = str(n)
	result = 0
	for i in stringed_num:
		result += int(i)
	print result
	return result

#n = int(raw_input("Enter an integer: "))

#int_sum(n)

# print "Printing range(2,5)", range(2,5)

def censor(text,word):
	split_text = text.split()
	N = len(split_text)
	for i in range(N):
		if word == split_text[i]:
			split_text[i] = "*" * len(word)
	result = " ".join(split_text)
	return result

print censor("My name is Jesus", "Jesus")
