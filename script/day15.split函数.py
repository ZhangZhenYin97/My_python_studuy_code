s = 'my name is zhang'
s2 = 'www.baidu.com'
s3 = 'www.baidu.com.cn'
'''split()默认是以空格符,/n /t 分割'''
data = s.split()
print(data)
data2 = s2.split('.')
print(data2)
'''指定分割次数'''
data3 = s.split(' ', 2)
print(data3)
data4 = s3.split('.',2)
print(data4)
'''分割两次或者两次以上可以取切片'''
data5 = s.split(' ', 2)[0]
print(data5)
data6 = s3.split('.',2)[2]
print(data6)