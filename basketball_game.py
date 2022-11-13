class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores=[]
        for i in range(len(operations)):
            if operations[i]=="D":
                if len(scores)>0:
                    scores.append(scores[len(scores)-1]*2)
            elif operations[i]=="C":
                tmp = scores.pop()
            elif operations[i]=="+":
                if len(scores)>1:
                    scores.append(scores[len(scores)-1]+scores[len(scores)-2])
                elif len(scores)==1:
                    scores.append(scores[len(scores)-1])
            else:
                scores.append(int(operations[i]))

        return sum(scores)