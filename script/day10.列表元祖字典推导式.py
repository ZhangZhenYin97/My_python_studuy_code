'''删选列表的偶数'''
list_ = [i for i in range(21) if i % 2 == 0]
print(list_)

'''筛选元组的奇数'''
tuple_ = [i for i in range(21) if i % 2 != 0]
print(tuple_)

'''筛选字典水果价格大于6的水果'''
dict_ = {
    'apple': 6,
    'orange': 8,
    'banana': 3,
    'watermelon': 9,
    'polo': 12
}
new_dict = {key: value for key, value in dict_.items() if value > 6}
print(new_dict)
