'''for 循环'''
sum_ = 0
for i in range(1, 101):
    sum_ += i

print(sum_)

'''sum 函数以及列表的推导式'''
print(sum([i for i in range(101)]))
