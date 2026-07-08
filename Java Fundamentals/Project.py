employees = [
    [1001, "Ashish", "01/04/2009", "e", "R&D", 20000, 8000, 3000],
    [1002, "Sushma", "23/08/2012", "c", "PM", 30000, 12000, 9000],
    [1003, "Rahul", "12/11/2008", "k", "Acct", 10000, 8000, 1000],
    [1004, "Chahat", "29/01/2013", "r", "Front Desk", 12000, 6000, 2000],
    [1005, "Ranjan", "16/07/2005", "m", "Engg", 50000, 20000, 20000],
    [1006, "Suman", "01/01/2000", "e", "Manufacturing", 23000, 9000, 4400],
    [1007, "Tanmay", "12/06/2006", "c", "PM", 29000, 12000, 10000]
]

def get_designation_and_da(code):
    match code:
        case "e":
            return "Engineer", 20000
        case "c":
            return "Consultant", 32000
        case "k":
            return "Clerk", 12000
        case "r":
            return "Receptionist", 15000
        case "m":
            return "Manager", 40000
        case _:
            return "Unknown", 0

emp_id = int(input("Enter Employee ID: "))

found = False

for emp in employees:
    if emp[0] == emp_id:
        found = True
        designation, da = get_designation_and_da(emp[3])
        salary = emp[5] + emp[6] + da - emp[7]
        print("Emp No.\tEmp Name\tDepartment\tDesignation\tSalary")
        print(f"{emp[0]}\t{emp[1]}\t\t{emp[4]}\t\t{designation}\t\t{salary}")
        break

if not found:
    print(f"There is no employee with empid : {emp_id}")