# map 函数
# 参数:map函数会创建一个容器,它的第一个函数是function 参数,第二个参数是一个可迭代对象
# 机制:里面的机制是使用for 循环用function函数接收可迭代对象的值然后返回给map 创建好的容器,它是一个obj 对象,可以使用list函数查看里面的内容
def add_func(n):
    return n * n


numbers = [1, 2, 3, 4, 5, 6]
data = map(add_func, numbers)
print(list(data))


# filter函数
# 参数:filter函数会创建一个容器,里面第一个参数是function参数,function函数会返回True,False,
# 机制:里面会for 循环可迭代对象的值,function会接收可迭代对象的值,如果是TRUE会存放到容器,FALSE则不会,可以用list 函数查看内容
def oushu_func(n):
    return n % 2 == 1


numbers_2 = [1, 2, 3, 4, 5, 6, 7]
data = filter(oushu_func, numbers_2)
print(list(data))
