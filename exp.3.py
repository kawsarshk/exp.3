# Program to calculate Gross Salary of an employee

# Input: Basic Salary
basic_salary = float(input("Enter the Basic Salary (BS): "))

# Allowances
DA = 0.70 * basic_salary   # Dearness Allowance = 70% of BS
TA = 0.30 * basic_salary   # Travel Allowance = 30% of BS
HRA = 0.10 * basic_salary  # House Rent Allowance = 10% of BS

# Gross Salary
gross_salary = basic_salary + DA + TA + HRA

# Output
print("\n--- Salary Details ---")
print(f"Basic Salary (BS): {basic_salary:.2f}")
print(f"Dearness Allowance (DA): {DA:.2f}")
print(f"Travel Allowance (TA): {TA:.2f}")
print(f"House Rent Allowance (HRA): {HRA:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")