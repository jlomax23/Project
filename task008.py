# Task 8
# Write a python function that accepts a string and calculate the number of upper case letters and lower case letters
def caseCount(text):
    upCount = 0
    loCount = 0

    for characters in analyzeText:
        if characters.isupper():
            upCount += 1
        elif characters.islower():
            loCount += 1
    return upCount, loCount

analyzeText = "Ask Not What Your Country Can Do For You but Ask What Can You Do For Your Country?"

upCase, loCase = caseCount(analyzeText)
print("\nHere is the text being analyzed: ", analyzeText)
print("\n\nThe number of uppercase letters are: ", upCase, "\n")
print("The number of lowercase letters are: ", loCase, "\n")
