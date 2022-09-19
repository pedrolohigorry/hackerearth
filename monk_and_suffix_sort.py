## Monk and Suffix Sort

## Problem from https://www.hackerearth.com/practice/codemonk/
## Section --> Sorting

inp = input().split(" ")
string = inp[0]
k = int(inp[1])

suffices = []

for i in range(len(string)):
    suffices.append(string[i:len(string)])

suffices.sort()
print(suffices[k-1])
