class Solution:
    def removeElement(self, nums, val):
        while True:
            try:
                nums.remove(val)
            except:
                return len(nums)
a = Solution()
print(a.removeElement([0,1,2,2,3,0,4,2],2))
