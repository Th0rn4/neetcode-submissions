class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l = list(t)

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in l:
                    l.remove(s[i])
                else:
                    return False
            else:
                return True
        else: 
            return False