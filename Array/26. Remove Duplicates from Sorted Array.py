class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while(i != len(nums) - 1 and len(nums)):
            if(nums[i] == nums[i+1]):
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)
    def removeDuplicates2(self, nums):
        index = cur = i = times = flag = 0
        while(i != len(nums)):
            if(i == 0):
                cur = nums[0]
                index = 0
                i += 1
            else:
                if(nums[i] != cur and nums[i-1] == cur):
                    index += 1
                    nums[index] = nums[i]
                    cur = nums[i]
                    i = i + 1
                    times = flag = 0
                elif(nums[i] != cur and nums[i-1] != cur):
                    i = i - 2**(times-1)
                    if(times < 2):
                        times = 0
                        flag = 1
                        i += 2 ** times
                elif(flag == 0):
                    i += 2**times
                    times += 1
                    if(i > len(nums) - 1):
                        i -= 2**(times-1)
                        times = 0
                        i += 1
                elif(flag == 1):
                    i += 1
        return index+1
    def removeDuplicates3(self, nums):
        new = set(nums)
        for i,num in enumerate(sorted(list(new))):
            nums[i] = num
        return len(new)
a = Solution()
print(a.removeDuplicates2([]))