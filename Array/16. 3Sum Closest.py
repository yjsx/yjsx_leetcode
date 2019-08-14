class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = 100000000
        for i in range(0,len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if(s < target):
                    if(abs(s - target)< abs(result - target)):
                        result = s
                    l += 1
                elif(s > target):
                    if (abs(s - target) < abs(result - target)):
                        result = s
                    r -= 1
                else:
                    return s
        return result


a = Solution()
print(a.threeSumClosest( [-1,0,1,1,55],3))

