## Monk being monitor

## Problem from https://www.hackerearth.com/practice/codemonk/ 
## Section --> Sorting

while t != 0:
    n = int(input())
    numbers = list(map(int, input().split()))

    ## Count frequency of occurrance of each number
    dictionary = {}
    for number in numbers:
        dictionary[number] = dictionary.get(number, 0) + 1

    ## To handle cases with one o more equal values
    ## For example: numbers = [2 2 2 2 2]
    if len(dictionary) == 1:
        print(-1)
        t-=1
        continue

    maximum = 1
    minimum = 1
    for k, v in dictionary.items():
        if v >= maximum:
            maximum = v
            key_maximum = k
        if v <= minimum:
            minimum = v
            key_minimum = k

    difference = dictionary[key_maximum] - dictionary[key_minimum]
    print(difference)
    t -= 1
