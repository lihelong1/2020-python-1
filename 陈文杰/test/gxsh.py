s1=set([1,2,3,4,5,6])
print(s1)
s1.update([7,9,10])
print(s1)
for i in range(1,10):
    for s in range(1,i+1):
        print('%d*%d=%d'%(s,i,i*s),end=' ')
    print()
import math
print(abs(-10))
math.pow(10,2)
print(int(round(0.1128,1)))
print("{:.1f}".format(0.1128))
print(sum([1,2,3,4]))
print(float(sum((1,3,45,5))))
x=str(sum([1,1.0,8.0]))
print(type("1"))
print(oct(10))
print(hex(10))
print(chr(98))
print(bin(10))
def persen(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
extra={'性别':'女'}
persen('cwj',18,**extra)

