import uuid
import hashlib

def get_random_str():
    # 获得uuid值
    uuid_val = uuid.uuid4()
    # 将uuid值转成字符串
    uuid_str = str(uuid_val).encode("utf-8")
    # 获得md5实例
    md5 = hashlib.md5()
    # 将uuid字符串做摘要
    md5.update(uuid_str)
    # 返回固定长度的字符串
    return md5.hexdigest()

import random
def get_random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)