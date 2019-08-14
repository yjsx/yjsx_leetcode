class Solution:
    def convert(self, s: str, numRows: int):
        if(numRows == 1):
            return s
        output = ""
        for i in range(numRows):
            j = i
            flag = 0
            while(j < len(s)):
                if(i == 0 or i == numRows - 1):
                    output += s[j]
                    j = j + (numRows-2)*2 + 2
                else:
                    output += s[j]
                    if(flag == 0):
                        flag = 1
                        j = j + (numRows - i - 1) * 2
                    else:
                        flag = 0
                        j = j + (i - 1) * 2 + 2
            i = i + 1
        return output
a = Solution()
s = a.convert('ABCDEFG',2)
print(s)
print(s == "PINALSIGYAHRPI")
