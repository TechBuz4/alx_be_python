# Objective: Implement a division calculator that robustly handles errors like division by zero 
# and non-numeric inputs using command line arguments.

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
