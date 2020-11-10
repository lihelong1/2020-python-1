scores={'语文':89,'数学':92,'英语':93}
print(scores)
empty_dict={}
print(empty_dict)
dict2={(20,30):'good',30:'bad'}
print(dict2)

list1=[1,1,22,33,4,4,55,6,66,7,7]
print('未转换的结果',list1)
list1=set(list1)
print('转换的结果',list1)

#n=int(input())
###i=1


n=int(input())
s=0
for i in range(1,n+1):
    t=1
    for j in range(1,i+1):
        t=t*j
        s=s+t
        print(s)