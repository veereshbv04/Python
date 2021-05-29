""" Selection sort is an optimised version of Insertion Sort,in shell sort
we reduce the number of swap that occur by moving heavier elements to the right"""

arr=[1,2,4,5]

def shell_sort(a):
    size=len(a)
    gap=size//2

    while gap>0:
        for i in range(gap,size):
            anchor=a[i]
            j=i
            while j>gap and a[j-gap]>=anchor :
                a[j]=a[j-gap]

            a[j]=anchor

        gap=gap//2

    return a
    
print(shell_sort(arr))
        
