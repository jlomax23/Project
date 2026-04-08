# Task 13
# Write a python program to count the number of lines in a text file.

f = open('Week4Labs.txt', 'r')
count = 0
for line in f:
    line = line.strip()
    count = count + 1
print('File Line Count: ', (count -1))