n=input()
maze=[[0 for i in range(n)] for j in range(n)]

x=raw_input()
cout=1
while(x!='-1'):
    sumOk = False
    r,c=map(int,x.split())
    maze[c-1][r-1]=1;
    for element in maze:
        if(sum(element)==n):
            print cout 
            sumOk = True
     
    cout+=1

    if sumOk:
        break
    
    x=raw_input()

if sumOk==False:
    print -1
    
