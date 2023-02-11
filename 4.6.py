def delchar(a,b):
    if len(b)!=1:
        return a
    else:
        return a.replace(b,"")
a="Good evening"
b=input("enter the character to be removed:")
print(delchar(a,b))

a="Take care"
b=input("enter the character to be removed:")
print(delchar(a,b))

a="123456s"
b=input("enter the character to be removed:")
print(delchar(a,b))

a="Red rose"
b=input("enter the character to be removed:")
print(delchar(a,b))

a="Flower"
b=input("enter the character to be removed:")
print(delchar(a,b))
