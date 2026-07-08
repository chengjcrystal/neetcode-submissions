class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = []
        for n in s:
            chars.append(n)
        for m in t:
            if m in chars:
                chars.remove(m)
            else:
                return False
        if chars:
            return False
        return True