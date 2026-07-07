gender = input("Enter gender (Male/Female): ")
age = int(input("Enter age: "))

if gender == "Female":
    if 1 <= age <= 58:
        print("Interest is 8.2%")
    elif 59 <= age <= 100:
        print("Interest is 9.2%")
elif gender == "Male":
    if 1 <= age <= 58:
        print("Interest is 8.4%")
    elif 59 <= age <= 100:
        print("Interest is 10.5%")