class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        countdict={}
        maxlen=0
        while r<len(s):
            countdict[s[r]]=countdict.get(s[r],0)+1 
            windowlen=(r-l)+1
            maxCount=max(countdict.values())
            repChar=windowlen-maxCount
            if repChar<=k:
                maxlen=max(maxlen,windowlen)
            else:
                while repChar>k:
                    countdict[s[l]]-=1
                    l+=1
                    windowlen=(r-l)+1
                    maxCount=max(countdict.values())
                    repChar=windowlen-maxCount
            
            r+=1

        return maxlen