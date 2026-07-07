ascii_codes = [int(x) for x in input("Enter ASCII codes separated by space: ").split()]

for code in ascii_codes:
    print(chr(code), end=" ")
print()