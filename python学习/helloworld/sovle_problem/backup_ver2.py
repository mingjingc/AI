import	os
import	time
#============================================
# 此程序假定在win10 下运行
# 与第一版的区别仅是为每天建立一个目录，
# 将文件打包在每天的目录中而已
#============================================

#  1.	需要备份的文件与目录将被
#	指定在一个列表中。
source	=	['D:\\junior',	'D:\\360CloudUI']
#	在这里要注意到我们必须在字符串中使用双引号
# 	用以括起其中包含空格的名称。

#2.	备份文件必须存储在一个 #主备份目录中
# 例如在	Windows	下：
target_dir	=	'D:\\Backup'
# 	要记得将这里的目录地址修改至你将使用的路径
#	如果目标目录不存在则创建目录
if	not	os.path.exists(target_dir):
    os.mkdir(target_dir)		#	创建目录

#	3.	备份文件将打包压缩成	zip	文件。
#	4.	将当前日期作为主备份目录下的子目录名称
today	=	target_dir	+	os.sep	+	time.strftime('%Y%m%d')
#	将当前时间作为	zip	文件的文件名
now	=	time.strftime('%H%M%S')
#	zip	文件名称格式
target = today + os.sep + now + '.zip'

#	如果目标目录还不存在，则进行创建
if	not	os.path.exists(today):
    os.mkdir(today) #	创建目录
    print('Successfully created directory', today)

#	5.	我们使用
# zip	命令将文件打包成	zip	格式
zip_command	=	'zip	-r	{0}	{1}'.format(target,	'	'.join(source))

#	运行备份
print('Zip	command	is:')
print(zip_command)
print('Running:')
if	os.system(zip_command)	==	0:
    print('Successful	backup	to',	target)
else:
    print('Backup	FAILED')
