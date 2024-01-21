class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        
        first_string, last_string = strs[0], strs[-1]
        
        for i, char in enumerate(first_string):
            if char != last_string[i]:
                return first_string[:i]

        return first_string

            