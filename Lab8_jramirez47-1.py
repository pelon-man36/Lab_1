"""
UPC Validator
Johan D. Ramirez Maldonado
This program will validate UPC codes
06/18/2026
"""
def find_UPC(code):
    odd_sum = 0
    even_sum = 0

    for i in range(0, 11, 2):
        odd_sum = int(code[i]) + odd_sum
    product = odd_sum * 3
    
    for i in range(1, 10, 2):
        even_sum = int(code[i]) + even_sum
    result = product + even_sum
    print(result)
    





ask_user = input("Enter a UPC code (must be 12 digits): ")
while len(ask_user) != 12:
    print("Invalid.")
    ask_user = input("Enter a UPC code (must be 12 digits): ")
find_UPC(ask_user)
