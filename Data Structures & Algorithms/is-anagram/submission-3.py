class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s.lower()) == len(t.lower())) :
            sorted_str1 = sorted(s)
            sorted_str2 = sorted(t)

            if sorted_str1 == sorted_str2:
                return True
            else:
                return False
        else:
            return False