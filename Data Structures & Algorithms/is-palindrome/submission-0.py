class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_rev = ""
        s_normal = ""
        for char in s:
            if char.isalnum():
                s_normal += char
                s_rev = char + s_rev
        return s_normal.lower() == s_rev.lower()