# Task 14
# Write a Python program to convert temperatures to and from Celsius and Fahrenheit [Formula: c/5=f-32/9 
# [where c = temperature in Celsius and f = temperature in Fahrenheit]]

import os
import platform
import math
# To clear the screen

def clearscr():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def performConversion(userInput):
    if userInput == 1:
        # User selected conversion from Celsius to Fahrenheit
        c = float(input("Please enter temperature for Celsius: "))
        # C to F > [(C * 9/5) + 32]
        toFAHR = float(c)
        conversion = (toFAHR * 9/5) + 32
    elif userInput == 2:
        # User selected conversion from Fahrenheit to Celsius
        f = float(input("Please enter temparture for Fahrenheit: "))
        # F to C > [(F - 32)] * 5/9
        toCEL = float(f)
        conversion = (toCEL - 32) * 5/9
    else:
        print("\n\nSorry, the input was invalid. Please try again.\n\n")
        return None
    return conversion

clearscr()

userinput = float(input("Enter 1) Celsius to Fahrenheit or 2) Fahrenheit to Celsius: "))

results = performConversion(userinput)
if results is not None:
    print("\n\nThe result is: ", results, "\n\n")
