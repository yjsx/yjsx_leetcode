class Solution:
    def myAtoi(self, str: str):
        if(len(str) == 0):
            return 0
        i = 0
        while(str[i] == ' '):
            i += 1
            if(i >= len(str)):
                break
        str = str[i:]
        if (len(str) == 0):
            return 0
        flag = 0
        if(str[0] == '-'):
            flag = 1
            str = str[1:]
        elif(str[0] == '+'):
            str = str[1:]
        i = 233
        for i in range(len(str)):
            if(str[i] >= '0' and str[i] <= '9'):
                continue
            else:
                i = i - 1
                break
        if(i == -1):
            return 0
        elif(i == 233):
            return 0
        else:
            if(flag == 0):
                return int(min(int(str[:i+1]),2**31 - 1))
            else:
                return int(max(-int(str[:i+1]),-2**31))
a = Solution()
print(a.myAtoi(" "))
