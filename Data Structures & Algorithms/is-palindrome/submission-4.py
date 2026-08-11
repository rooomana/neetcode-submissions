class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        odd_check = len(s) % 2
        middle = len(s) // 2
        return s[:middle] == s[:middle - 1 + odd_check:-1]