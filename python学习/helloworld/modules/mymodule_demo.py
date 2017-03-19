#包的作用
# 从Finder中的目录就可以看出来，每个package实际上是一个目录（Directory),那么IDE是怎么
# 识别它为package呢？没错，__init__.py的第一个作用就是package的标识，如果没有该文件，该
# 目录就不会认为是package
# 首先是一个python文件，所有还可以用来写python模块
# 但是不建议这么写，尽量保证__init__.py足够轻
from modules import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)
