def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    left , right = 0 , x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x <= mid * mid:
            right = mid
        else:
            left = mid + 1#如果不加1，mySqrt(1)就会陷入死循环，所以一笔+1 使得左大于右，跳出循环

print(mySqrt(19))

