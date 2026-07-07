nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

result = [x for x in nums if x != 10]
while len(result) < len(nums):
    result.append(0)

print(result)