# 工具方法，可以像dictA 中 加入 dictB的内容
def mergeDict(dictA, dictB):
    dictA.update(dictB)

def get_dict_attr(dict, attr):
    if dict.__contains__(attr):
        return dict[attr]
    return None

def get_int(obj):
    if not obj:
        return None
    if type(obj).__name__ == 'int':
        return obj
    if type(obj).__name__ == 'str':
        return int(obj)
    return None

def confusion(str):
    str = str.replace("_", "", 3).lower()
    if str.endswith('s'):
        str = str[0:len(str) - 1]
    return str

def similar(str1, str2):
    if not type(str1).__name__ == 'str' or not type(str2).__name__ == 'str':
        return False
    if not str1 or not str2:
        return False
    str1 = confusion(str1)
    str2 = confusion(str2)
    if str1 == str2:
        return True
    return False

def similar_find_in (str1, str2):
    if not type(str1).__name__=='str' or not type(str2).__name__=='str':
        return False
    if not str1 or not str2:
        return False
    str1 = confusion(str1)
    str2 = confusion(str2)
    if not str2.find(str1) >=0 :
        return False
    return True