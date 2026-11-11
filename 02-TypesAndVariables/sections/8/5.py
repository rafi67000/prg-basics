###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#

def display_info(_swift):
    print(f"""
Code: {_swift}
Bank Code: {_swift[:4]}
Country Code: {_swift[4:6]}
    """)

codes = ["BPKOPLPW", "CHASUS33", "DEUTDEFF"]

swift = input('Enter SWIFT code: ')
display_info(swift)

for code in codes:
    display_info(code)

