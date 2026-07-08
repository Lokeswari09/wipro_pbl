class Calculator:
    @staticmethod
    def power_int(num1, num2):
        return int(math.pow(num1, num2))

    @staticmethod
    def power_double(num1, num2):
        return math.pow(num1, num2)

import math

n1 = int(input("Enter base integer: "))
n2 = int(input("Enter exponent integer: "))
d1 = float(input("Enter base double/decimal: "))

print("Result of power_int:", Calculator.power_int(n1, n2))
print("Result of power_double:", Calculator.power_double(d1, n2))