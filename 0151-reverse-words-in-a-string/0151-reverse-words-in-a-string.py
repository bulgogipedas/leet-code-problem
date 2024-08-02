class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()

        reverse = word[::-1]

        reversed_s = ' '.join(reverse)
        return reversed_s
        