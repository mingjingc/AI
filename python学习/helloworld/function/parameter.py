# def	print_max(a,	b):
#     if	a	>	b:
#         print(a,	'is	maximum')
#     elif	a	==	b:
#         print(a,	'is	equal	to',	b)
#     else:
#         print(b,	'is	maximum')
# #	直接传递字面值
# print_max(3,	4)
# x	=	5
# y	=	7
# #	以参数的形式传递变量
# print_max(x,	y)

# 当我们声明一个诸如		*param		的星号参数时，从此处开始直到结束的所有位置参数
# （Positional	Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
# 类似地，当我们声明一个诸如		**param		的双星号参数时，从此处开始直至结束的所有关键字
# 参数都将被收集并汇集成一个名为		param		的字典（Dictionary）。
def	total(a=5,	*numbers,	**phonebook):
    print('a',	a)
	#遍历元组中的所有项目
    for	single_item	in	numbers:
        print('single_item',	single_item)
	#遍历字典中的所有项目
    for	first_part,	second_part	in	phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231))

