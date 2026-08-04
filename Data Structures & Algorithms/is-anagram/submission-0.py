class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        for i, c in enumerate(s):
            if c != t[i]:
                return False
        return True
        