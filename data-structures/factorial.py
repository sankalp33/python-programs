def fact(number):
    if number==0:
        return 1
    else:
        return number*fact(number-1)

n=int(input("Enter a number to find its factorial:"))
print("The Factorial of ",n," is:",fact(n))
