def main():
	d = {'one': 1, 'two': 2}

	for k in d:
		print(k, d[k])

	for k in sorted(d.keys()):
		print(k, d[k])

if __name__ == "__main__": main()
			
