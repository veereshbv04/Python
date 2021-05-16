# BRUTE FORCE METHOD
# TIME COMPLEXITY IS O(b)

def power(a,b): 
    p=a;
    for i in range(2,b+1):
       p=p*a
    return p
    

print(power(2,3))
