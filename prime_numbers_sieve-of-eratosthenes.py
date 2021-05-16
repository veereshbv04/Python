# complexity is BIG O(NloglogN)
# to find prime numbers upto "n"

def sieveOfEratosthenes(n):
    prime=[ True for i in range(n+1)]
    prime[0]=False
    prime[1]=False
    p=2
    while( p * p < n):
        if prime[p]==True :
            for i in range(p*2,n+1,p):
                prime[i]=False

        p+=1

    for p in range(n+1):
        if prime[p] :
            print(p)


sieveOfEratosthenes(15)
        
