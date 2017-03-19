# 当我们在 Person 类下创建新的实例 p 时，我们采用的方法是先写下类的名称，后跟括在
# 括号中的参数，形如： p = Person('Swaroop') 。
# 我们不会显示地调用 __init__ 方法。 这正是这个方法的特殊之处所在。
class Person:
    def __init__(self, name):
        self.name = name  #self类似java的this
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Swaroop')
p.say_hi()