class TimeMap:

    def __init__(self):
        self.timemap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.timemap[key])==0:
            return ""
        l=0
        r=len(self.timemap[key])-1
        ans=""
        while l<=r:
            mid=l+(r-l)//2
            if self.timemap[key][mid][1]<= timestamp:
                ans=self.timemap[key][mid][0]
                l=mid+1
            else:
                r=mid-1
        return ans
        
