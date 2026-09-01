class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().strip()
        mod=""
        for ch in s:
            if ch.isalnum():
                mod+=ch
        print(mod)
        i=0
        j=len(mod)-1
        while i<j:
            if mod[i]!=mod[j]:
                return False
            i+=1
            j-=1
        return True
