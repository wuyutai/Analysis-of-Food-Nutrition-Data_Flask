# 哈希加盐方法加密
import re
import time

from werkzeug.security import generate_password_hash, check_password_hash


# 时间戳转格式化
def time_format(timestamp):
    if timestamp:
        time_tuple = time.localtime(timestamp)
        result = time.strftime("%Y-%m-%d", time_tuple)
        return result
