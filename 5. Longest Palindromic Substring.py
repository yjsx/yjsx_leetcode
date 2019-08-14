class Solution:
    def longestPalindrome(self, s: str):
        tmp = list(s)
        s = '#'.join(tmp)
        s = '$#'+s+'#'
        Len = []
        for i in range(len(s)):
            Len.append(0)
        max_len = -1

        loc = 0
        id = 0
        mx = 0
        for i in range(len(s) - 1):
            i = i + 1
            if (i < mx):
                Len[i] = min(Len[2 * id - i], mx - i)
            else:
                Len[i] = 1
            while(i + Len[i] <= len(s) - 1 and s[i - Len[i]] == s[i + Len[i]]):
                Len[i] += 1
            if (mx < i + Len[i]):
                id = i
                mx = i + Len[i]
            if(max_len < Len[i] - 1):
                max_len = Len[i] - 1
                loc = i
        return s[loc-max_len:loc+max_len + 1].replace('#','')
a = Solution()
print(a.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))