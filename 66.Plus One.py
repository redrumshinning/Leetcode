def plusOne(digits):
    sum = 0
    for i in range(len(digits)):
        sum += digits[i] * (10 ** (len(digits) - i - 1))

    sum += 1
    output = []

    for i in range(len(str(sum))):
        a = sum % 10
        sum = sum // 10
        output.insert(0, a)

    return output

def plusOne2(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))#pow(x,y) 等于 x**y
    return [int(i) for i in str(num+1)]

print(plusOne2([1,2,3]))

