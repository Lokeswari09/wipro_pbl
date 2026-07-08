import sys

if len(sys.argv) < 3:
    print("Please provide two string arguments.")
else:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print(arg1 + " Technologies " + arg2)