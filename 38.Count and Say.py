def countAndSay(n):
    s = '1'
    for i in range(n - 1):
        new, temp, count = s[0],'',0
        for num in s:
            if num == new:
                count += 1
            else:#不相等时，先把前面的存下来，然后将要计算的数字存为new，初始化个数为1，再计算new有几个
                temp += str(count) + new
                new = num
                count = 1
        temp += str(count) + new
        s = temp
    return s

print(countAndSay(5))