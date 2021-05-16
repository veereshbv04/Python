# finding power of a number using DIVIDE AND CONQUER method
# TIME COMPLEXITY IS O(LOG B)

def power(a,b):
    if b==0: return 1
    elif b%2==0 :
        halfpower=pow(a,b//2)
        return halfpower*halfpower
    else :
        halfpower =pow(a,b//2)
        return halfpower*halfpower*a

print(power(2,5))
