a=[]
b=[]
n=int(input('enter a first list no.of elements'))
for i in range(n):
    m=int(input('enter the values'))
    a.append(m)
print(a)
c=int(input('enter the secondlist no.of elements'))
for i in range(c):
    o=int(input('enter the values'))
    b.append(o)
print(b)
          
a.extend(b)
print(a)
a.sort()
print(a)
