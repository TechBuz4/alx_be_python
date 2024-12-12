# calculate and provide feedback on a user’s monthly savings 
#  Financial Details
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses
rate = 0.05

# Project Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)

print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
