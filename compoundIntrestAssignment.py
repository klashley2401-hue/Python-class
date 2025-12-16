#kevin Lashley
#compound interest assignment
#Professor Chelo Gerhardson
#Python-115
#october 12, 2025


# Import the math module for the power function
import math

# Get user input for the variables
pv = float(input("Enter the principal investment (PV): "))
r_percent = float(input("Enter the annual interest rate in percent (R): "))
t = float(input("Enter the number of periods in years (t): "))
m = int(input("Enter the number of times compounding occurs per period (m): "))

# Convert the interest rate from percentage to decimal
r = r_percent / 100

# Calculate the future value using the compound interest formula
fv = pv * math.pow((1 + r / m), (m * t))

# Print the result formatted to two decimal places with a dollar sign
print(f"The future value (FV) is: ${fv:.2f}")