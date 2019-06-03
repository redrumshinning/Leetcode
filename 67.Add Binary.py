def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if a == '0' and b == '0':
        return '0'
    a = To10(a)
    b = To10(b)
    sum = a + b
    return To2(sum)


def To10(digits):
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i]) * pow(2, len(digits) - 1 - i)
    return sum


def To2(a):
    c = []

    while a > 0:
        c.append(a % 2)
        a = a // 2
    output = ''
    for i in range(len(c)):
        output += str(c.pop())
    return output

def addBinary2(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    num1 = int(a, base=2)#num = int(a,base) 表示num的base进制为a
    num2 = int(b, base=2)
    res = num1 + num2
    s = str(bin(res))#转化为二进制，前面有ob
    return s[2:]

print(addBinary2('11','1'))

