# calculate and provide feedback on a user’s monthly savings 
#  Financial Details
monthly_income = input("Enter your monthly income:")
monthly_expense = input("Enter your total monthly expenses:")

# Calculate Monthly Savings
monthly_savings = float(monthly_income) - float(monthly_expense)
rate = 0.05

# Project Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
