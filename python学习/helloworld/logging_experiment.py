import os
import platform
import logging

# os.path.join函数来将这三部分位置信息聚合到一起。使用
# 这一特殊函数，而非仅仅将这几段字符串拼凑在
# 一起的原因是这个函数会确保完整的位置路径符
# 合当前操作系统的预期格式。
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')
print("Logging to", logging_file)

# 配置 logging 模块，让它以特定的格式将所有信息写入我们指定的文件
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")