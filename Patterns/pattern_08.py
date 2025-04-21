n=5
for i in range(n):
    for s in range(i):
        print(' ',end=" ")
    for j in range(2*n-(i*2+1)):
        print('*',end=" ")
    for p in range(i):
        print(' ',end=" ")
    print()