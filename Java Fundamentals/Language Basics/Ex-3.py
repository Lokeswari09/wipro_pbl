import sys

if len(sys.argv) < 3:
    print("Please provide two integer arguments.")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2
    print("The sum of", num1, "and", num2, "is", total)