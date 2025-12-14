from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
       students_q = deque(students)
       sandwiches_q = deque(sandwiches)

       failed = 0  #number of consecutive students couldn't eat lunch
       while students_q and failed < len(students_q):
        if students_q[0] == sandwiches_q[0]:
            students_q.popleft()
            sandwiches_q.popleft()
            failed = 0
        else:
            students_q.append(students_q.popleft())
            failed += 1
        
       return len(students_q)



