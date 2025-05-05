n=10


for i in range(1,n*2):
    if(i<=n):
        for j in range(i):
            print("*",end="")
    if(i>n):
        for j in range(n*2-i):
            print("*",end="")
    print()        
            
