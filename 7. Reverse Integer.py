class Solution:
    def reverse(self, x: int):
        if(x >= 0):
            return self.over_zero(str(x))
        else:
            return -self.over_zero(str(x)[1:])
    def over_zero(self,x):
        return int(x[::-1])
a = Solution()
print(a.reverse(0))
