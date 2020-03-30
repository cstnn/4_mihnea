"""
Do a simple math operation !
BUT make it interractive...
"""

# Define initial variables
print(":::::::: In order to perform the math operation, YOU (the user) need to provide the values !")
a = input("What is the value of <a> ? >>> ")
b = input("What is the value of <b> ? >>> ")

# Define the operation and run it
# !!!! Converting the user inputs from string (text) to integer (numbers)
c = int(a) + int(b)

# Print the result
print("The result is : ", c)
