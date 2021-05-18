# fibinocci series
# Recursion Method
# TIME COMPLEXITY IS 2**N
# EXPONENTIAL TIME COMPLEXCITY

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))
