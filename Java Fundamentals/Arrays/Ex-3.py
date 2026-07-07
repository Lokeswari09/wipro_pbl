nums = [int(x) for x in input("Enter array elements separated by space: ").split()]
search = int(input("Enter the number to search: "))

if search in nums:
    print(nums.index(search))
else:
    print(-1)