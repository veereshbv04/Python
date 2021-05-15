# prime numbers between two numbers
n=int(input("enter n value"))
m=int(input("enter m value"))
l=[]
for i in range(n,m):
    if i>1:
        for j in range(2,i):
            if i%j==0 :
                break
        else:
            print(i)
            l.append(i)
            print(len(l))
