def climbstairs(n):
    steps=[]
    steps.append(1)
    steps.append(2)
    print(steps)
    for i in range(2,n):
        steps.append(steps[i-1]+steps[i-2])
        print(steps)
    return steps[n-1]
n=int(input('enter no.of stairs'))
print(climbstairs(n))
    
