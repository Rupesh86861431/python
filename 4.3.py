def smallernumber(n):
    c=[0]*len(n)
    for i in range(len(n)):
        for j in range(len(n)):
            if(n[i]>n[j]):
                c[i]+=1
    return c
print(smallernumber([1,2,3,5,5,6]))
                
