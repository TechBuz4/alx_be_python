# Objective: Implement a division calculator that robustly handles errors like division by zero 
# and non-numeric inputs using command line arguments.

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
