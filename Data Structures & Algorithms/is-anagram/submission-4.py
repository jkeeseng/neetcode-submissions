class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for num in s: 
            if num in dic: 
                dic[num] += 1
            else: 
                dic[num] = 1
        for letter in t: 
            if letter in dic: 
                dic[letter] -= 1 
            else: 
                return False 
        return all (value == 0 for value in dic.values())
