class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in dictionary: 
                return [dictionary[j], i]
            else: 
                dictionary[nums[i]] = i


        