# Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.


def safe_divide(numerator, denominator):
    try:
        # 1. Conversion is attempted first. If this fails (non-numeric input), 
        #    a ValueError is raised, and the flow jumps to 'except ValueError'.
        num = float(numerator)
        denom = float(denominator)
        result = num / denom  # 2. Division is attempted next. If denom == 0, a ZeroDivisionError is raised.
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # if denom == 0: # This check is redundant due to the exception handling
        # the zero division error is caught here
        # in other words, python raises this exception automatically when a division by zero is attempted
        return "Error: Cannot divide by zero."
    except ValueError:
        # This block executes ONLY if the conversion to float failed (non-numeric input).
        return "Error: Please enter numeric values only."