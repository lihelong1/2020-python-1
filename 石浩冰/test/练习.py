#s1=set=(1,2,3)
#print(s1)
l1=[1,2,3,4,5]
s1=set(l1)





t2=(1,2,3,4,3,2)
s2=set(t2)


s3={1,2,3,4}
l3=list(s3)
print(l3)

t3=(1,2,3,4)
l4=tuple(t3)
print(l4)

l=[1,1,2,3,4,4,5]
l=list(set(l))
print(l)



for n in range(100,200):
    i=n//100


    j=n//10%10
    k=n%10
    if n ==i**3+j**3+k**3:
        print(n)