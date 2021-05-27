def cumulative_sum(li):
    cur=li[0]
    max_value=0
    for i in range(1,len(li)):
        cur+=li[i]
        if cur > max_value:
            max_value=cur
    return max_value 
            
            
            

li=[1,4,-2,2,1,2]
print(cumulative_sum(li))
