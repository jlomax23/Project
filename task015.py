# Task 15
# Write a function that takes a list value as an argument and returns a string with all the items separated by comma and a space, with and inserted before the last item.

# For example, given the following list: mylist : ['ford' 'Chevy', 'honda', 'dodge']
# The function would returnL 'ford, chevey, honda, and dodge'

def chgLine(theList):
    if len(theList) == 1:
        return theList[0]
    elif len(theList) >= 2:
        outcome = ""
        # List all but last item
        for item in theList[:-1]:
            outcome = outcome + item + ", "
        # Add the "and" part last
        outcome = outcome + "and " + theList[-1]
        return outcome

theList = ["Ford", "Chevy", "Honda", "Dodge", "Volkswagen", "Nissan"]
print("\n", chgLine(theList), "\n")
