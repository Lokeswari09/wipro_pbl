class InvalidEmployeeException(Exception):
    pass
emp = input()
if emp == "None" or not emp.strip():
    emp = None
if emp is None:
    raise InvalidEmployeeException("Employee is null")
else:
    print(f"Employee: {emp}")