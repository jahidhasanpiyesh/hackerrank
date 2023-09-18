"""
Problem link>>>>>>>https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
"""

n = int(input())
arr = list(set(sorted(map(int, input().split()))))  # convert to set and list
arr.sort()  # dont miss to sort()>>>functions
print(arr[-2])  # index -2 position just print out
