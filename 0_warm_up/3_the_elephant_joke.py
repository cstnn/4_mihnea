"""
1. How do you put an Elephant in the fridge ?
- You check if the fridge is empty
- You take the Elephant and you put it in the fridge

2. How do you put a Crocodile in the fridge ?
- You check if the fridge is empty
- You take the Elephant out
- You take the Crocodile and you put it in the fridge
"""


# Define variables and their content
fridge = []
elephant = 'Elephant'
crocodile = 'Crocodile'


##########################################
#  1. ADD Elephant in the <fridge>
##########################################
print("\n:::::::: [1] Trying to put the ELEPHANT in the FRIDGE")

# Check if <fridge> is empty
print("1.1 - Checking if the fridge is empty")
if fridge == []:
    
    # Put the Elephant in the <fridge>
    print("1.2 - The fridge is empty >> Putting Elephant in the fridge !")
    fridge.append(elephant)
    
    # Print fridge content
    print("1.3 - Fridge content is now :", fridge)
    
    
# If the <fridge> is not empty then print a message and the fridge content
else:
    print("      [ERROR] Something is in the fridge :", fridge)
    
        
##########################################
#  2. ADD Crocodile in the <fridge>
##########################################
print("\n:::::::: [2] Trying to put the CROCODILE in the FRIDGE")

# Check if <fridge> is empty
print("2.1 - Checking if the fridge is empty")
if fridge == []:
        
    # Put the Crocodile in the <fridge>
    print("2.2 - The fridge is empty >> Putting Crocodile in the fridge !")
    fridge.append(crocodile)
    
# If the <fridge> is not empty then print a message and the fridge content
else:
    print("      [ERROR] Something is in the fridge :", fridge)
    
    # Removing Elephant from the <fridge>
    print("2.3 - Removing Elephant from the fidge", fridge)
    fridge.remove(elephant)
    
    # Put the Crocodile in the <fridge> after is empty
    print("2.4 - The fridge is empty NOW >> Putting Crocodile in the fridge !")
    fridge.append(crocodile)
    
    # Print fridge content
    print("2.5 - Fridge content is now :", fridge)
    