nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

nums.sort()

print("Smallest two:", nums[0], nums[1])
print("Largest two:", nums[-2], nums[-1])