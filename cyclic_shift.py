'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.8

Monk and Inversions
Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size  for his birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells  such that .
Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.

Input:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.

Output:
Print the answer to each test case in a new line.

Constraints:
1 <= T <= 100
1 <= N <= 20
0 <= M [i][j] <= 1000


Sample Input
2  ## amount of tescases
3  ## testcase 1, a matrix of 3 x 3
1 2 3  ## the 3 x 3 matrix
4 5 6
7 8 9
2  ## testcase 2, a matrix of 2 x 2
4 3
1 4
Sample Output
0
2

'''

############ Solution using Python 3.8
############ Solution using Python 3.8
t = int(input())  # save the number of testcases

while t != 0:


    ## save the numbers of items and number of rotations
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]

    string = input()

    max_number = string

    ## calculate all cyclic shifs
    for i in range(1,n+1):
        new_string = string[i:n] + string[0:i]
        if int(new_string) > int(max_number):
            max_number = int(new_string)

    count_max = 0
    for i in range(1,n+1):
        new_string = string[i:n] + string[0:i]

        if int(new_string) == max_number:
            count_max += 1
            i_max = i

        if count_max == 2:
            print(i)
            break

        if i == n:
            print( n * (k-1) + i_max)


    t -= 1
