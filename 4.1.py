fizzbuzz=int(input('enter the number'))
for i in range(1,fizzbuzz+1):
    if i %15==0:
        print('fizzbuzz')
        continue
    elif i%3==0:
        print('fizz')
        continue
    elif i%5==0:
        print('buzz')
        continue

    print(str(i))
