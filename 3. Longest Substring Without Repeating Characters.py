class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        dic = {}
        for i, ch in enumerate(list(s)):
            if(ch not in dic.keys()):
                dic[ch] = -1
            if(dic[ch] >= start):
                if(i == 0):
                    longest += 1
                else:
                    if(i - dic[ch]> longest):
                        longest = i - dic[ch]
                    start = dic[ch] + 1
                    dic[ch] = i
            else:
                dic[ch] = i
                if (i - start + 1 > longest):
                    longest = i - start + 1
        return longest