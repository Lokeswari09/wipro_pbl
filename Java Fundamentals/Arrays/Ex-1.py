nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

total = sum(nums)
avg = total / len(nums) if nums else 0

print("Sum:", total)
print("Average:", avg)