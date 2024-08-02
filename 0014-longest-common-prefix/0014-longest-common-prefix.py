class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(i) for i in strs) ## looping len terkecil di list

        answer = ""
        for i in range(min_len):
            char = strs[0][i]
            if all(strs == char for i in strs):
                answer += char
            else:
                break
            