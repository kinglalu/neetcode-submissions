class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = ""
        for i in range(len(s)):
            if s[i].isalnum():
                string1+=s[i].lower()
        
        string2 = ""

        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                string2+=s[i].lower()

        return string1 == string2
        
        
        