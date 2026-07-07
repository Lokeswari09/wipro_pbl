args = input("Enter values separated by space (or leave empty): ").split()

if len(args) == 0:
    print("No values")
else:
    print(",".join(args))