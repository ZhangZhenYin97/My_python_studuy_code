'''元组拆包'''
student_info = ('andy', 'male', 18, 2004, 5, 31)
name, gender, age, *birthday = student_info
print(name)
print(gender)
print(age)
print(birthday)


'''列表拆包'''
teacher_info = ['july', 'female', 60, 1962, 6, 2]
name, gender, age, *birthday = teacher_info
print(name)
print(gender)
print(age)
print(birthday)
