nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
valid = True

for x in nums:
    if x != 1 and x != 4:
        valid = False
        break

print(valid)