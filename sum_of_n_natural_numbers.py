# program to find the sum of n natural numbers
# TIME COMPLEXITY IS O(N)

def sum_of_n(n):
    s=0
    for i in range(1,n+1):
        s+=i

    return s




# below method is done using recursion
# this is similar to spoting seat in a theater problem
def sum_of_n_using_recursion(n):
    if n==1 :
        return 1
    else:
        return sum_of_n_using_recursion(n-1) + n



print(sum_of_n(6))
print(sum_of_n_using_recursion(4))
