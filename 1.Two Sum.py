class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if(nums[i] not in dic.keys()):
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        for x in nums:
            if(target - x in dic):
                if(x == target / 2):
                    if(len(dic[x]) != 1):
                        return dic[x]
                    else:
                        continue
                return [dic[x][0],dic[target-x][0]]