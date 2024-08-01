class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        cleaned = ''.join(char for char in lower if char.isalnum())
        return cleaned == cleaned[::-1]