"""
Problem link>>>>>>>https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
"""

n = int(input())
arr = list(set(sorted(map(int, input().split()))))
arr.sort()
print(arr[-2])
