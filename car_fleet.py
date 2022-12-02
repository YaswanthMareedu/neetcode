class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d={}
        for i in range(len(position)):
            d[position[i]]=speed[i]
        position.sort(reverse=True)
        stack = []
        for i in range(len(position)):
            stack.append((target - position[i]) / d[position[i]])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
