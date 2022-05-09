list_ = [i for i in range(101)]
new_list = []
for i in list_:
    if str(i)[-1] == '1':
        new_list.append(i)

print(new_list)

