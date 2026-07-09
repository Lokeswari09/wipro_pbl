def addLastDigits(input1, input2):
    last1 = abs(input1) % 10
    last2 = abs(input2) % 10
    return last1 + last2

num1 = int(input())
num2 = int(input())
print(addLastDigits(num1, num2))