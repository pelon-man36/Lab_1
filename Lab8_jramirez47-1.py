"""
UPC Validator
Johan D. Ramirez Maldonado
This program will validate UPC codes
06/18/2026
"""
def find_UPC(code):
    print("This is a placeholder for now")



ask_user = input("Enter a UPC code (must be 12 digits): ")
while len(ask_user) != 12:
    print("Invalid.")
    ask_user = input("Enter a UPC code (must be 12 digits): ")
find_UPC(ask_user)
