t=input()

for a0 in xrange(t):
    n,k=map(int,raw_input().split())
    sizes=[]
    for a1 in xrange(n):
        sizes.append(input())
    
    sizes.sort()

    if(k==1):
        print (sizes[(len(sizes)-1)]-sizes[0])

    else:
        x = [sizes[i]-sizes[i-1] for i in range(1,n)]
        y = list(x)
        y.sort()

        total=sum(y[0:n-k])
        print total
        
##        array=[0]*n
##        for a2 in range(1,n-k+1):
##            temp=y[a2-1]
##            index=x.index(temp)
##            x[index]=-1
##            if(array[index]==0 and array[index+1]==0):
##                array[index]= a2
##                array[index+1]=a2
##            elif(array[index]!=0 and array[index+1]==0):
##                array[index+1]=array[index]
##            elif(array[index]==0 and array[index+1]!=0):
##                array[index]=array[index+1]
##            else:
##                copy=array[index+1]
##                while(array[index+1]==copy):
##                    array[index+1]=array[index]
##                    index=index+1

            
        

    
   
    
