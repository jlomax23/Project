# Task 12
# Write a python function to read and print the first n lines of a file.

def printNfiles(filename, nth):
	f = open(filename, "r")
	
	for i in range(nth):
		line = f.readline()
		if not line:
			break
		print(line.rstrip('\n'))

userTotal = int(input("\n\nHow many lines would you like to read? "))

fn = "Week4Labs.txt"

printNfiles(fn, userTotal)