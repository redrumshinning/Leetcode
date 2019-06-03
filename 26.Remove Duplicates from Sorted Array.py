def removeDuplicates(nums):#注意题目是排好序的列表，所以相同数字也是相邻的！
    """
    :type nums: List[int]
    :rtype: int
    """

    length = len(nums)
    if length == 0:
        return 0

    internal = 0
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:#当前后两个数不相等时，间隔不加1，但是i加了1，所以
            internal += 1
            length -= 1
        nums[i - internal] = nums[i]
    return length

def removeDuplicates2(A):#相当于有两个指针，一个指向循环的值i，一个指向待插入位置，如果这两个位置的值
    if not A:            #不同，那么将待插入位置前进一位并赋值(先+1再赋值，与27题区别）
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]

    return newTail + 1
print(removeDuplicates2([1,2,2,2,4,5,5,6]))