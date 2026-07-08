address = input()
if address == "None" or not address.strip():
    address = None
print(address if address is not None else "India")