
def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)




result = fact(int(input("Enter a number: ")))

print(result)



def fib (num):
    if num == 1:
        return  0
    elif num == 2:
        return 2
    return fib(num-1) + fib(num - 2)

number = fib(10)

print(number)
