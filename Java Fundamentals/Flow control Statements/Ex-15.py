user_input = input("Enter an integer: ")

if not user_input:
    print("Please enter an integer number")
else:
    n = int(user_input)
    for i in range(1, n + 1):
        print("*  " * i)