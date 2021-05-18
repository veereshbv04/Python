# Finding Fibinocci of a Number
# Using Dynamic Programinng
# TIME COMPLEXITY IS O(N)
# SPACE COMPLEXITY IS O(N)


n=int(input("Enter the number"))
fibarray=[-1 for i in range(0,n+1)]
fibarray[0]=0
fibarray[1]=1
def fib_dp(n):

    if fibarray[n]!=-1 :
        return fibarray[n]
    else:
        fibarray[n]=fib_dp(n-1)+fib_dp(n-2)
        return fibarray[n]


print(fib_dp(9))
