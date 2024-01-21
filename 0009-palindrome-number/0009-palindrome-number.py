class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        b = x[::-1]
        return(x == b)