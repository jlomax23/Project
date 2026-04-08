# Task 5
# Calculate the length of a string

# Get a string from user
getUserInfo = input("Type any sentence here: ")

# Calculate the length of user's input
StringLength = getUserInfo.strip()

# Display the length
print("The length of:\'", getUserInfo, "\' is:", len(StringLength), "character(s) long")
