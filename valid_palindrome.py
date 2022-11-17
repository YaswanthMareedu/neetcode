class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp=''
        for i in s:
            if (i>='a' and i<='z') or (i>='A' and i<='Z') or (ord(i)>=48 and ord(i)<=(48+9)):
                if (ord(i)>=48 and ord(i)<=(48+10)):
                    tmp+=i
                else:
                    tmp+=i.lower()
        #print(tmp)
        return tmp==tmp[::-1]