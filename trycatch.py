#gettig user input for a number and peroforming divison
try:
    numerator  = float(input("enter the numerator:"))
    denominator = float(input("enter the denominator:"))
    result = numerator*denominator
    print("result:",result)
except ZeroDivisionError:
    print("error: cannot divide by zero")
except ValueError:
    print("error : invalid input, please enter valid numbers.")
except Exception as e:
    print("an unexpected error accurred:", e)