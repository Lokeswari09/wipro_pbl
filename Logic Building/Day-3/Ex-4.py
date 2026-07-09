def secondLastDigit(input1):
    num_str = str(abs(input1))
    if len(num_str) < 2:
        return -1
    return int(num_str[-2])

num = int(input())
print(secondLastDigit(num))