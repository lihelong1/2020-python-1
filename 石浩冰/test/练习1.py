sxh = 100
while sxh <=999:
    a= sxh % 10
    b=sxh //10%10
    c=sxh//100
    if sxh ==a**3+b**3+c**3:
        print (sxh)
    sxh+=1

print(oct(10))


str='final exam'
print(str[0])
print(str[0].upper())
print(str[1:-1])
print(str[1:])
print(str[1:5])

dec=int(input('请输入数字：'))
print('八进制的数:',oct(dec))
print('二进制的数：',bin(dec))
print('十六进制的数：',hex(dec))











