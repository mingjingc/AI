age	=	20
name	=	'Swaroop'
#类似于C的格式输出，一一对应
#format		方法所做的事情便是将每个参数值替换至格式所在的位置
# print('{1}	was	{0}	years	old	when	he	wrote	this	book'.format(name,	age))
# print('Why	is	{0}	playing	with	that	python?'.format(name))

# #你可以通过		end	=''	指定其应以空白结尾
# #	对于浮点数	'0.333'	保留小数点(.)后三位
# print('{0:.3f}'.format(1.0/3))
# #	使用下划线填充文本，并保持文字处于中间位置 #	使用	(^)	定义	'___hello___'字符串长度为	11
# print('{0:_^11}'.format('hello'))
# #基于关键词输出	'Swaroop	wrote	A	Byte	of	Python'
# print('{name}	wrote	{book}'.format(name='Swaroop',	book='A	Byte	of	Python'))

print('what\'s your name?')
#新的一行
r"Newlines	are	indicated	by	\n"
print(r'\1')