import sys

if len(sys.argv) < 2:
    print("Please provide a name.")
else:
    name = sys.argv[1]
    print("Welcome " + name)