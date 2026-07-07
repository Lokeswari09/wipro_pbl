nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

total = 0
skip = False

for num in nums:
    if num == 6:
        skip = True
    if not skip:
        total += num
    if num == 7 and skip:
        skip = False

print(total)