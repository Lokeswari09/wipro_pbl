elements = [int(x) for x in input("Enter 4 numbers separated by space: ").split()]

if len(elements) != 4:
    print("Please enter 4 integer numbers")
else:
    print("The given array is:")
    print(elements[0], elements[1])
    print(elements[2], elements[3])
    
    elements.reverse()
    
    print("The reverse of the array is:")
    print(elements[0], elements[1])
    print(elements[2], elements[3])