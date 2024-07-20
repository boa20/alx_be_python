def safe_divide(numerator, denominator):
    try:
        quotient = float(numerator) / float(denominator)
        return f"The result of the division is {quotient}"
    except ValueError:
        return f"Error: Please enter numeric values only."
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."