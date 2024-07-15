def safe_divide(numerator, denominator):
    try:
        quotient = int(numerator) / int(denominator)
        print(f"The result of the division is {quotient}")
    except ValueError:
        print(f"Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")