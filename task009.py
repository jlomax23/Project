# Task 9
# Write a python program that matches a string that has an a follow by zero or more b's

import re 

pattern = r"^ab*$" 

tStrings = ["a", "bbab", "abb", "abbb", "b", "ba", "aab", "ab0", "ab00", "00ab", "a"] 

for s in tStrings: 
    if re.fullmatch(pattern, s): 
        print(f"{s!r} matches") 
    else: 
        print(f"{s!r} does NOT match")