class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        flag=0
        res=0
        ans=0
        for i in range(len(tokens)):
            if tokens[i]=='*' or tokens[i]=='+' or tokens[i]=='-' or tokens[i]=='/':
                flag=1
                if len(stack)>=2:
                    #print(stack)
                    b=stack.pop()
                    a=stack.pop()
                    a=int(a)
                    b=int(b)
                    if tokens[i]=='*':
                        res=a*b
                        stack.append(str(res))
                    elif tokens[i]=='+':
                        res=a+b
                        stack.append(str(res))
                    elif tokens[i]=='-':
                        res=a-b
                        stack.append(str(res))
                    elif tokens[i]=='/':
                        if a>0 and b<0:
                            b=-b
                            res=a//b
                            res=-res
                        elif a<0 and b>0:
                            a=-a
                            res=a//b
                            res=-res
                        else:
                            res=a//b

                        #print(a,b,res)
                        stack.append(str(res))
                    #print(stack)
            else:
                stack.append(tokens[i])
            
        if flag==0 and len(tokens)>0:
            return int(tokens[0])
        else:
            return res