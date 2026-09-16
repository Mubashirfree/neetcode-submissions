class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1={}
        for ch in s1:
            counts1[ch]=1+counts1.get(ch,0)
        counts2={}
        l=0
        r=0
        while r<len(s2):
            counts2[s2[r]]=counts2.get(s2[r],0)+1
            if r-l+1 ==len(s1):
                if counts1==counts2:
                    return True
                else:
                    counts2[s2[l]]-=1
                    if counts2[s2[l]]==0:
                        counts2.pop(s2[l])
                    l+=1
            r+=1    
        return False