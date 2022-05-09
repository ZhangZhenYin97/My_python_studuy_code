'''
1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
重写__str__方法，返回student的信息。
3、创建Teacher类，继承Person类，属性有学院college，专业professional
，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’
'''


class Person:
    def __init__(self, name, age, gender):
        self.name = name,
        self.age = age,
        self.gender = gender

    def personInfo(self):
        print(f'我的名字是:{self.name},性别{self.gender},今年{self.age}岁了')


class Student(Person):
    def __init__(self, college, class_,name,age,gender):
        super().__init__(name,age,gender)
        self.college = college,
        self.class_ = class_

    def personInfo(self):
        print(f'我的名字是:{self.name},性别{self.gender},今年{self.age}岁了,来自{self.college}学院，{self.class_}班级')

    def study(self, teacher):
        print(f'我今天学会了{teacher.teach()}')


class Teacher(Person):
    def __init__(self, college, professional,name,age,gender):
        super().__init__(name,age,gender)
        self.college = college,
        self.professional = professional

    def personInfo(self):
        print(f'我的名字是:{self.name},性别{self.gender},今年{self.age}岁了,是{self.college}专业,{self.professional}班级的老师')

    def teach(self):
        return "面向对象编程"


s = Student('张三', 18, '男', '信息工程学院', '软工一班')
teacher = Teacher('李老师', 35, '女', '信息工程学院', 'python')
s.study(teacher)
