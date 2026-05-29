class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        res = nums[0]
        maxCount = 0
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else: 
                my_dict[num] += 1
            if my_dict[num] > maxCount:
                res = num 
                maxCount = my_dict[num]
        return res