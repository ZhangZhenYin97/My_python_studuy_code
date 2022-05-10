list_ = [1, 2, 3, 4, 4, 3, 5]
new_list = []
for i in list_:
    if i%2 != 0:
        new_list.append(i)

print(new_list)

data = list(filter(lambda i : i %2 != 0, list_))
print(data)

