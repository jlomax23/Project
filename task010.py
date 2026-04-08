# Task 10
# Write a python script to check if a given key already exists in a dictionary
myDict = {"name": "Alice", "age": 30, "city": "New York"}

keyCheck = "age"

if keyCheck in myDict:
    print(f"Key '{keyCheck}' does exist in the dictionary.")
else:
    print(f"Key '{keyCheck}' does NOT exist in the dictionary.")