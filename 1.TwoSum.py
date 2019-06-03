def twoSum(nums,target):
    for i in range(len(nums)):
        sub = target - nums[i]
        for j in range(i+1, len(nums)):
            if sub == nums[j]:
                return [i, j]
def twoSum2(nums,target):
    mapping = {}

    for index, val in enumerate(nums):
        diff = target - val
        if diff in mapping:
            return [index, mapping[diff]]
        else:
            mapping[val] = index

List=[3,2,4]
target = 6
print(twoSum2(List,target))