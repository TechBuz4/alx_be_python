# calculate and provide feedback on a user’s monthly savings 
#  Financial Details
income = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")

# Calculate Monthly Savings
savings = int(income) - int(expenses)
rate = 0.05

# Project Annual Savings
projected_savings = savings * 12 + (savings * 12 * 0.05)

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")