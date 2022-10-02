k, l = map(int,input().split())
student = dict()
for i in range(l):
  stu_num = input()
  student[stu_num] = i

student_sort = sorted(student.items(),key=lambda x: x[1])
if len(student) < k:
  k = len(student)
for j in range(k):
  print(student_sort[j][0])