n= 5 
char = 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(char),end=" ")
    char +=1
    print()