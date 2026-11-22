class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1  

        while left < right:

            while self.alphaNum(s[left]) is False and left < right:
                left += 1
            
            while self.alphaNum(s[right]) is False and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -=1
        return True
        

    def alphaNum(self, c):
        res = (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9') )


        return res
        
