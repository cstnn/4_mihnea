"""
How do you put your shoe laces to  your shoes ?
1. Take the fist shoe
2. Loop the lace through all the holes

3. Take the second shoe
2. Loop the lace through all the holes
"""

# Define the variables
shoes = ['Left','Right']
lace_holes = [1,2,3,4,5,6]

print("\n:::::::: Starting to put the laces on your shoes")

# Create LOOP 1 - for each shoe
for shoe in shoes:
    # Print what is being done - going through each shoe
    print("\n::: Starting to work on", shoe, "shoe")
       
    # Create LOOP 2 - for each lace hole
    for lace_hole in lace_holes:
        # Print what is being done - going through each lace hole
        print("    Inserting the lace into hole ", lace_hole)
    print("---", shoe, "shoe is DONE !")

# 
print("\n::: ALL shoes have shoe laces now !!!")