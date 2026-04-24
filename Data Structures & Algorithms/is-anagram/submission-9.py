class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        dict = {}

        for num in s:
            if num in dict:
                dict[num] += 1
            else: 
                dict[num] = 1
        
        for num in t:
            if num not in dict:
                return False 
            else:
                dict[num] -= 1 


        for values in dict.values(): # [0,2,3]
            if values != 0:
                return False 
        
        return True 
