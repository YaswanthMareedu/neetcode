class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        while True:
            if students[0]!=sandwiches[0]:
                tmp=students[0]
                students.pop(0)
                students.append(tmp)
            else:
                students.pop(0)
                sandwiches.pop(0)
            dummy=False
            for i in range(len(students)):
                if students[i]==sandwiches[0]:
                    dummy=True
                    break
            if dummy==False:
                return len(students)

        return 0