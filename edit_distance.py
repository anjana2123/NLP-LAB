'''The code Implementation for the edit distance algorithm'''
##Importing Packages
import numpy as np
import string as st

##Defining the cost meterics for the Operations
insertion_cost = 1
deletion_cost = 1
substitution_cost = 2


##Function to calculate the edit distance
def lev_distance(text_1,text_2,opeartions = []):
    """Returns the Edit Distance and the set of operations to be performed for the
    two sequences given to the Function"""
    
    if (len(text_2) == 0):
        ##If the text_2 is empty the cost would be the length of the text_1 to convert
        opeartions+= ([f'Delete {text_1} from text_1'] if len(text_1) else [])
        return len(text_1),opeartions
    
    if (len(text_1) == 0):
        opeartions+= ([f'Insert {text_2} from text_1'] if len(text_2) else [])
        return len(text_2),opeartions
    
    if text_1[0] == text_2[0]:
        opeartions+= [f'Make no change for the char {text_1[0]}']
        return lev_distance(text_1[1:], text_2[1:],opeartions)

    ##Calculate the cost if the Insertion Operations Appears
    insertion_operations = opeartions + [f'Insert {text_2[0]} in text_1']
    insertion,insertion_operations = lev_distance(text_1, text_2[1:],insertion_operations)
    
    ##calculate the cost if the Deletion Operations Appears
    deletion_operations = opeartions + [f'Delete {text_1[0]} from text_1']
    deletion,deletion_operations = lev_distance(text_1[1:], text_2,deletion_operations)
    
    ##Calculate the cost if the Subsition Operation Appears
    substitution_operations = opeartions + [f'Replace {text_1[0]} in text_1 with {text_2[0]}']
    substitution,substitution_operations = lev_distance(text_1[1:], text_2[1:],substitution_operations)
    
    
    ## Calculate the Minimum Cost among all the one
    min_cost = min(
        insertion+insertion_cost,
        deletion+deletion_cost,
        substitution+substitution_cost
        )
    
    if min_cost == (substitution+substitution_cost):
        return min_cost,substitution_operations
    
    elif min_cost == (deletion+deletion_cost):
        return min_cost,deletion_operations
    
    else:
        return min_cost,insertion_operations
    
##Driver Block
text_1 = "Muthu"
text_2 = "Mewchew"

cost,operations = lev_distance(text_1, text_2)
print(f"The Cost between {text_1} and {text_2}: {cost}")
print("Operations")
for operation in operations:
    print(operation)