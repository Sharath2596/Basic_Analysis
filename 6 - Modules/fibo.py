# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
 
def odorev(n):
    if (n%2)==0:
        print ("Even Number")
    else:
        print ("Odd Number")
