shoplist	=	['apple',	'mango',	'carrot',	'banana']
name	=	'swaroop'
#	Indexing	or	'Subscription'	operation	#
# #	索引或“下标（Subcription）”操作符
print('Item	0	is',	shoplist[0])
print('Item	1	is',	shoplist[1])
print('Item	2	is',	shoplist[2])
print('Item	3	is',	shoplist[3])
print('Item	-1	is',	shoplist[-1])  #倒数第一个
print('Item	-2	is',	shoplist[-2])
print('Character	0	is',	name[0])

#	Slicing	on	a	list
print('Item	1	to	3	is',	shoplist[1:2:3])  # 右开区间，第三个参数为步长
print('Item	2	to	end	is',	shoplist[2:])
print('Item	1	to	-1	is',	shoplist[1:-1])
print('Item	start	to	end	is',	shoplist[:])

#	从某一字符串中切片
print('characters	1	to	3	is',	name[1:3])
print('characters	2	to	end	is',	name[2:])
print('characters	1	to	-1	is',	name[1:-1])
print('characters	start	to	end	is',	name[:])
