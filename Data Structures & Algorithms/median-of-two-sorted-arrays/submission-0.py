class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedarr=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                sortedarr.append(nums1[i])
                i+=1
            else:
                sortedarr.append(nums2[j])
                j+=1
        if i<len(nums1):
            for k in range(i,len(nums1)):
                sortedarr.append(nums1[k])
        else:
            for k in range(j,len(nums2)):
                sortedarr.append(nums2[k])
        print(sortedarr)
        if len(sortedarr)%2==0:
            mid=len(sortedarr)//2
            ans=(sortedarr[mid-1]+sortedarr[mid])/2
            return ans
        else:
            mid=len(sortedarr)//2
            return sortedarr[mid]