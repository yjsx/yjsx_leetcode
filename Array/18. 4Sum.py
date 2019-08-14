class Solution:
    def fourSum(self, nums, target) :
        nums = sorted(nums)
        results = []
        self.nSum(4,nums,target,[],results)
        results = set(map(str,results))
        results = list(map(self.str_to_list,results))
        return results
    def str_to_list(self,a):
        a = a[1:-1].split(',')
        return list(map(int, a))
    def nSum(self,n, nums, target, result_head, results):
        if(n == 2):
            l, r = 0, len(nums) - 1
            while(l<r):
                s = nums[l] + nums[r]
                if(s < target):
                    l += 1
                elif(s > target):
                    r -= 1
                else:
                    results.append(result_head + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while(l < r and nums[l-1] == nums[l]):
                        l += 1
                    while(l < r and nums[r+1] == nums[r]):
                        r -= 1
        else:
            for i in range(len(nums)-n+1):
                self.nSum(n - 1, nums[i + 1:],target - nums[i], result_head+[nums[i]],results)
a = Solution()
print(a.fourSum([-1,0,-5,-2,-2,-4,0,1,-2],-9))