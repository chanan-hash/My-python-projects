a = 5
b = 2


try:
    print("resource Open")
    print(a/b)

    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print(a+b)
    print("Hey, you cannot divide a number by Zero, ",e)

except ValueError as e:
    print("Invalid Input,", e)

except Exception as e:
    print("Something went wrong..." , e)

finally:
    print("resource Closed")

print("Bye")


