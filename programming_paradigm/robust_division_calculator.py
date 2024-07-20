def safe_divide(numerator, denominator):
    try:
        quotient = float(numerator) / float(denominator)
        f"The result of the division is {quotient}"
    except ValueError:
        print(f"Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")