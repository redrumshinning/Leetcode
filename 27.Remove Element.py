def removeDuplicates(nums,val):
    length = len(nums)
    if length == 0:
        return 0
    point = 0
    for i in range(0,len(nums)):
        if nums[i] != val:      #如果相等，point不动，先赋值再前进
            nums[point] = nums[i]
            point += 1
    return point,nums

print(removeDuplicates([1,2,2,3,4,6,7,2],2))
