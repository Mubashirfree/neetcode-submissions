class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        key1={}
        key2={}
        unique=set(s)
        if len(s)!=len(t):
            return False
        for ch in s:
            key1[ch]=key1.get(ch,0)+1
        for ch in t:
            key2[ch]=key2.get(ch,0)+1
        for ch in unique:
            if key1.get(ch,0)!=key2.get(ch,0):
                return False
        return True
