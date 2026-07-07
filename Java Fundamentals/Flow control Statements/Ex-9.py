months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

user_input = input("Enter month number: ")

if not user_input:
    print("Please enter the month in numbers")
else:
    m = int(user_input)
    if 1 <= m <= 12:
        print(months[m - 1])
    else:
        print("Invalid month")