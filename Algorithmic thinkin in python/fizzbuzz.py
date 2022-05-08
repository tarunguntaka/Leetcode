
#3 - fizz, 5 buzz, both fizz buzz

a = [i for i in range(1,101)]
for i in range (0,100):
    if a[i]%3 ==0 and a[i]%5 ==0:
        a[i] ='fizz, buzz'
    else:
        if a[i]%3 ==0:
            a[i]='fizz'
        elif a[i]%5 ==0:
            a[i] ='buzz'

print(a)