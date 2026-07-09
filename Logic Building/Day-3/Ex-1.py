def isEven(input1):
    if input1 % 2 == 0:
        return 2
    else:
        return 1

num = int(input())
print(isEven(num))