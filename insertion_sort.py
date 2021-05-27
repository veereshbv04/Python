# TIME COMPLEXITY IS O(N**2)

a=[4,2,6,1,2,541,6,4,63,24,43]

def insertion_sort(a):
    for i in range(1,len(a)):
       key =a[i]
       j=i-1
       while a[j]>=key and j>=0:
           a[j+1]=a[j]
           j-=1

       a[j+1]=key

    return a

        
print(insertion_sort(a))
