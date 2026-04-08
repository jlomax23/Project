# Task 3
# Get input from user (Prompt user to provide list of comma list)
# Split by commas
# Convert into list
# Convert into tuple

getUserInput = input("Enter a comma-separated list of numbers: ")
getValues = getUserInput.split(",")

getTuple = tuple(getValues)

print("Comma List:", getUserInput)
print("Tuple List:", getTuple)