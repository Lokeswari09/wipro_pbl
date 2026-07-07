nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]

print(evens + odds)