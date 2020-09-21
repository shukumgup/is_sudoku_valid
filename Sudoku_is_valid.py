from collections import defaultdict
n = int(input())
for i in range(n):
    arr = [int(x) for x in input().split()]
    matrix_r = [[0 for k in range(9)] for l in range(9)]
    matrix_c = [[0 for k in range(9)] for l in range(9)]

    flag = 0
    for j in range(9):
        for k in range(9):
            matrix_r[j][k] = arr[9*j + k]
            matrix_c[k][j] = arr[9*j + k]
        for j in range(9):
        data = defaultdict(int)
        for k in range(9):
            val = matrix_r[j][k]
            data[val] = data[val] + 1
            for l in range(9):
                if val !=0 and val == matrix_c[k][l] and (j != l):
                    #print(j,k,l)
                    flag = 1
                    break

            if val != 0 and data[val] > 1:
                flag =1
            if flag ==1:
                break
        if flag ==1:
            break
    if flag == 1:
        print(0)
    else:
        print(1)