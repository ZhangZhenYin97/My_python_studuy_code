'''
找出列表重复数据
list_ = [1, 0, 2, 3, 4, 7, 5, 5]

'''

list_ = [1, 0, 2, 3, 4, 7, 5, 5, 7, 1, 0]

new_list = []
k = 0
for i in list_:
    k += 1
    for j in list_[k:]:
        if i == j:
            new_list.append(j)
print(new_list)

'''去除列表重复数据'''
print(set(list_))
