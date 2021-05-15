def checkIfPrime(n):
    if n<=1 :return "Not Prime"
    else:
        for i in range(2,n//2):
            if(n%i==0):
                break
        else:
            
            return "Prime"

k=5

print(checkIfPrime(k))
