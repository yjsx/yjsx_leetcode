class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        c = nums1 + nums2
        c = sorted(c)
        if(len(c)%2 == 0):
            return (c[int(len(c)/2)] + c[int(len(c)/2) - 1]) / 2
        else:
            return float(c[int(len(c) / 2) ])

a = Solution()
print(a.findMedianSortedArrays([1,3,5],[2,4]))
