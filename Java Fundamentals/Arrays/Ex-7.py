nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_nums = []

for x in nums:
    if x not in unique_nums:
        unique_nums.append(x)

print(unique_nums)