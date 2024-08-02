class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', "", s).lower()
        return cleaned == cleaned[::-1] 