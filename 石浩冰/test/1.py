'''
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib(10))

def fib(n):
    if n == 1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))


def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
        return fibs
    print(fib(10))


a = [1,2,3]
b = a[:]
print (b)


for i in range(1,10):
    print
    for j in range(1,i+1):
        print('%d*%d=%d' %(i,j ,j*i))

import time
myD={1:'a',2:'b'}
for key,value in dict.items(myD):
    print(key,value)
    time.sleep(1)



'''
import time
print (time.strftime('%y-%m%d %H:%M:%S',time.localtime(time.time())))
time.sleep(2)
print (time.strftime('%y-%m%d %H:%M:%S',time.localtime(time.time())))


def rab(num):
    f1 = 1
    f2 = 2
    if num ==1 or num==2:
        return 1
    else:
        for i in range(num-1):
            f1,f2 = f2,f1+f2
        return f1
    print(rab(36))



