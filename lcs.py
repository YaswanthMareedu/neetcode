class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t = {}
        s1,s2 = text1,text2
        def lcs(s1,s2,n,m,t):
            if n<=0 or m<=0:
                return 0
            if (n,m) in t:
                return t[(n,m)]
            
            if s1[n-1]==s2[m-1]:
                t[(n,m)] = 1+lcs(s1,s2,n-1,m-1,t)
            else:
                t[(n,m)] = max(lcs(s1,s2,n-1,m,t),lcs(s1,s2,n,m-1,t))

            return t[(n,m)]
        
        #return lcs(s1,s2,len(s1),len(s2),t)
