def isValid(s):

    mapping = {')':'(',']':'[','}':'{'}
    stack = [None]#必须赋值None，不然如果s第一个就为右括号的话，stack在pop报错
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if mapping[i] != stack.pop():
                return False

    if len(stack) > 1:
        return False
    else:
        return True

print(isValid(']'))

