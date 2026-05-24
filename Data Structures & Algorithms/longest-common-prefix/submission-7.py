class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(strs)
        prefix = strs[0]

        for i in range(1,len(strs)):
            shortest_length = min(len(prefix), len(strs[i]))
            prefix = prefix[:shortest_length]
            for j in range(0,len(prefix)):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
        return prefix

