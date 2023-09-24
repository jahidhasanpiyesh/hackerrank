"""
Problem link >>>> https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
"""

N = int(input())
data = []
for i in range(N):
    cmd = input().split()  # data bag
    # using for index and access to index data
    if cmd[0] == "insert":
        data.insert(int(cmd[1]) , int(cmd[2]))
    elif cmd[0] == "print":
        print(data)
    elif cmd[0] == "remove":
        data.remove(int(cmd[1]))
    elif cmd[0] == "append":
        data.append(int(cmd[1]))
    elif cmd[0] == "sort":
        data.sort()
    elif cmd[0] == "print":
        print(data)
    elif cmd[0] == "pop":
        data.pop()
    elif cmd[0] == "reverse":
        data.reverse()
    elif cmd[0] == "print":
        print(data)
