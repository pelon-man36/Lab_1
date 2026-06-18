"""
UPC Validator
Johan D. Ramirez Maldonado
This program will validate UPC codes
06/18/2026
"""
def find_UPC(code):
    """This function will validate UPC codes.
    
    Args:
        code (str): A string of 12 digits that represents a UPC code.
    Returns:
        Prints whether the final digit of the user inputed UPC is valid or not, 
        and if not valid, what it should be.
    """
    odd_sum = 0
    even_sum = 0

    for i in range(0, 11, 2):
        odd_sum = int(code[i]) + odd_sum
    product = odd_sum * 3
    
    for i in range(1, 10, 2):
        even_sum = int(code[i]) + even_sum
    result = product + even_sum
    
    true_result = result % 10
    if true_result != 0:
        true_result = 10 - true_result
    
    if true_result == int(code[-1]):
        print(f"{true_result} is a valid final digit for UPC code.")
    else:
        print(f"{code[-1]} is not a valid final digit for the UPC code.")
        print(f"{true_result} is what was calculated to be the valid digit for the UPC code.")

    





ask_user = input("Enter a UPC code (must be 12 digits): ")
while len(ask_user) != 12:
    print("Invalid.")
    ask_user = input("Enter a UPC code (must be 12 digits): ")
find_UPC(ask_user)
