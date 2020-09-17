n = int(input())
t=""
for i in range(n):
    data = str(input())
    length=len(data)
    stack = []
    op=[]
    num = 1
    for j in range(length+1):
        stack.append(num)
        num = num + 1
        if j == length or data[j] =='I':
            while len(stack)!=0:
                op.append(stack[-1])
                stack.pop()
    #print(op)
    print(t.join(str(x) for x in op))