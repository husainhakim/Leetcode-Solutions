from statistics import median 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined=nums1+nums2
        sortedlist=sorted(joined)
        return median(sortedlist)
        