t=int(input('enter total users'))
s=int(input('enter staff users'))
n=s/3
if(t<1):
    print('invalid input')
else:
    st=t-(s+n)
    print('student users are',st)
