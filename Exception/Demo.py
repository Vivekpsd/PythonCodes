a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError as e:
    print("Something went wrong")
    print(e)
finally:
    print("must execute")


try:
    data = int(input("Enter number: "))
except Exception as e:
    print("Must input integer not string", e)
