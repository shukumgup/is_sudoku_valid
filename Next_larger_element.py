n = int(input())
for i in range(n):
    m = int(input())
    stack_1 = []
    arr = [int(x) for x in input().split()]
    for j in range(m-1,-1,-1):
        while(len(stack_1) != 0 and stack_1[-1]<arr[j]):
            stack_1.pop()
        t = arr[j]
        if (len(stack_1)==0):
            arr[j] = -1
        else:
            arr[j] = stack_1[-1]
        stack_1.append(t)
    print(*arr)