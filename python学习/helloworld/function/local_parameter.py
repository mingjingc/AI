#所有变量的作用域是它们被定义的
x	=	50
def	func(x):
    print('x	is',	x)
    x	=	2
    print('Changed	local	x	to',	x)
func(x)
print('x	is	still',	x)
