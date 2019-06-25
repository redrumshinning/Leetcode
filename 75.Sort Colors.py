class Solution(object):#[1,0,2,1,1,0] -> [0,1,2,1,1,0] -> [0,1,0,1,1,2]->[0,0,1,1,1,2]
    def sortColors(self, nums):
        """
        red代表0，white代表1，blue代表2（三个指针）
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1