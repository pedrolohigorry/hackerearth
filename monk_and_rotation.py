'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.8

Monk and Rotation
Monk loves to preform different operations on arrays, and so being the
principal of Hackerearth School, he assigned a task to his new student Mishki.
Mishki will be provided with an integer array A of size N and an integer K ,
where she needs to rotate the array in the right direction by K steps and then
print the resultant array. As she is new to the school, please help her to
complete the task.

Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of
elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements
of the array A.

Output:
Print the required array.

Constraints:
1 <= T <= 20
1 <= N <= 10 ** 5
0 <= K <= 10 ** 6
0 <= Array

Sample Input
1
5 2
1 2 3 4 5
Sample Output
4 5 1 2 3
'''

############ Solution using Python 3.8
t = int(input())  # save the number of testcases
while t != 0:
    ## save the numbers of items and number of rotations
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]

    ## save the number of arrays as a list
    array = list(map(int, input().split()))

    ## define index, if k > n, then we do more than 1 full rotation, so we keep only with the modulo we keep only the extra part of 1 full rotation
    index = n - (k%n)

    ## building the rotation of the array
    for i in range(index, n):
        print(array[i], end = " ")
    for i in range(index):
        print(array[i], end = " ")
    print("")  ## This is needed so that for each testcase (each t) we don't add a new line

    ## We do it for each test case
    t -= 1
