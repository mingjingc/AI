#	这是一个字符串对象
name	=	'Swaroop'
if	name.startswith('Swa'):
    print('Yes,	the	string	starts	with	"Swa"')
if	'a'	in	name:
    print('Yes,	it	contains	the	string	"a"')
if	name.find('war')!=	-1:
    print('Yes,	it	contains	the	string	"war"')

#=============================================
# str
# 类同样还拥有一个简洁的方法用以
# 联结（Join）    序列中的项目，其中字符串
# 将会作为每一项目之间的分隔符
delimiter	=	'_*_'
mylist	=	['Brazil',	'Russia',	'India',	'China']
print(delimiter.join(mylist))
