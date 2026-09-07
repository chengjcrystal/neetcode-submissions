class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower()
        
        a = 0
        b = len(clean) - 1

        #abba aba

        while a <= b:
            if clean[a] != clean[b]:
                return False
            a += 1
            b -= 1
        
        return True

        