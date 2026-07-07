elements = [int(x) for x in input("Enter 9 numbers separated by space: ").split()]

if len(elements) != 9:
    print("Please enter 9 integer numbers")
else:
    print("The given array is:")
    print(elements[0], elements[1], elements[2])
    print(elements[3], elements[4], elements[5])
    print(elements[6], elements[7], elements[8])
    
    print("The biggest number in the given array is", max(elements))