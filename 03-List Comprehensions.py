"""
Problem link:>>>>>>>https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
"""
# remove the comments for input function >>>>>>>
x = int(input("Enter the first input:"))
y = int(input("Enter the second input:"))
z = int(input("Enter the thread input:"))
n = int(input("Enter the condition input != data:"))

# data = 5
# for i in range(data+1):
#     print(i)   # 0 1 2 3 4 5  index wys data insert
# conditions >>>  [i, j, k] wys data in comprehensions

result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
print("Output is hear :", result)




