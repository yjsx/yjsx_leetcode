class Solution:
    def isPalindrome(self, x: int):
        if(x < 0):
            return False
        l  = len(str(x))
        print(l)
        f = int("".join(reversed(list(str(int(x / 10**int(l / 2)))))))
        if(l % 2 == 0):
            s = int(str(x % 10**int(l / 2)))
        else:
            s = int(str(x % 10**(int(l / 2) + 1)))
        print(f,s)
        if(f == s):
            return True
        else:
            return  False
a = Solution()
print(a.isPalindrome(12021))