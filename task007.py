# Task 7
# Write function that multiply all the numbers in a list
import math
# Create the function to calculate the list
def CountMe(getValues):
    #get the values
    g = getValues
    # Calculate the user's input
    xx = 1
    for caluser in getValues:
        xx *= int(caluser)
    return xx

x = input("Enter a list of comma-separated numbers: ")
getValues = x.split(",")

#call function
ttt = CountMe(getValues)

print("\nMultiplying everything in the list equals", ttt, "\n\n")
