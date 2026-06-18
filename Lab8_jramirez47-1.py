"""
UPC Validator
Johan D. Ramirez Maldonado
This program will validate UPC codes
06/18/2026
"""
def find_UPC(code):
    odd_sum = 0
    for i in range(0, 11, 2):
        odd_sum = int(code[i]) + odd_sum
    print(odd_sum)




ask_user = input("Enter a UPC code (must be 12 digits): ")
while len(ask_user) != 12:
    print("Invalid.")
    ask_user = input("Enter a UPC code (must be 12 digits): ")
find_UPC(ask_user)
