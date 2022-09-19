## Monk and Nice Strings

## Problem from https://www.hackerearth.com/practice/codemonk/ 
## Section --> Sorting

n = int(input())
old_strings = []

while n != 0:
    s = input()
    count = 0

    ## In this if we handle the base case
    if old_strings == []:
        old_strings.append(s)
        n -= 1
        print(0)
        continue

    ## Loop through older strings. Only count those smaller than current string.
    for letter in old_strings:
        if s > letter:
            count += 1
    print(count)
    old_strings.append(s)

    n -= 1
