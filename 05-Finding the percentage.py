"""
Problem Link >>>>>https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
"""
n = int(input())
student_marks = {}
for _ in range(n):
    name , *line = input().split()  # input data bag use to split()
    scores = list(map(float , line))  # line data convert to list
    student_marks[name] = scores
query_name = input()

data = 0
for i in student_marks[query_name]:
    data = data + i  # increment to one gor
result = data / len(student_marks[query_name])  # condition >> data / n
print("{0:.2f}".format(result))