class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        count = [0] * 26 
        for word in strs:
            sorted_word = sorted(word)
            print(sorted_word)
            key = ''.join(sorted(word))
            if key not in my_dict:
                my_dict[key] = [word]
            else: 
                my_dict[key].append(word)
        return list(my_dict.values())