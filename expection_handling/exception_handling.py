"""
exception ==> An Event that interrupts the flow of a program
              (ZeroDivisonError, TypeError, ValueError)
              1.try, 2.except, 3.finally
"""

try:
    number = int(input("enter number to divide:  "))
    print(f"{1/number:.2f}")
except ZeroDivisionError:
    print(f"enter the value more than zero")
# except ValueError:
#     print(f"enter the number only")
except Exception as e:
    print(f"entered into exception {e}")

finally:
    print("do the cleanup")