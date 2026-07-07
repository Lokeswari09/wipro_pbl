ch = input("Enter a character: ")

if ch.islower():
    print(ch + "->" + ch.upper())
else:
    print(ch + "->" + ch.lower())