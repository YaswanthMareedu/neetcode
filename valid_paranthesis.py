class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        flag1,flag2=False,False
        for i in range(len(s)):
            if s[i]=='(':
                flag1=True
                stack.append(s[i])
            elif s[i]=='{':
                flag1=True
                stack.append(s[i])
            elif s[i]=='[':
                flag1=True
                stack.append(s[i])
            elif s[i]=='}':
                flag2=True
                if len(stack)==0:
                    return False
                if len(stack)>0 and stack.pop()!="{":
                    return False
            elif s[i]==']':
                flag2=True
                if len(stack)==0:
                    return False
                if len(stack)>0 and stack.pop()!="[":
                    return False
            elif s[i]==')':
                flag2=True
                if len(stack)==0:
                    return False
                if len(stack)>0 and stack.pop()!="(":
                    return False

        if len(stack)==0 and flag1==True and flag2==True:
            return True
        else:
            return False
