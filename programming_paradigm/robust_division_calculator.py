# Objective: Implement a division calculator that robustly handles errors like division by zero 
# and non-numeric inputs using command line arguments.

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
        return None
