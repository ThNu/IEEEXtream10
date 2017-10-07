t=input()

for a0 in xrange(t):
    p,s,n=map(int,raw_input().split())
    access=[]
    for a1 in xrange(n):
        access.append(input()/s)

    
    fifo=[]
    m=0
    fi=0
    for item in access:
        if item not in fifo:
            if m<p:
                fifo.append(item)
                m=m+1
            else:
                fi=fi+1
                fifo.append(item)
                fifo.remove(fifo[0])

    lru=[]
    m=0
    lr=0
    for item in access:
        if item not in lru:
            if m<p:
                lru.append(item)
                m=m+1
            else:
                lr=lr+1
                lru.append(item)
                lru.remove(lru[0])
        if item in lru:
            lru.append(item)
            lru.remove(item)

    if lr>=fi:
        print "no",fi,lr
    else:
        print "yes",fi,lr
            
        


##x=raw_input().split()
##tot=0
##k=1
##l=1
##for i in xrange(len(x)):
##    if(i==0):
##        tot+=1
##        k=1
##    if(i>0):
##        if(x[i]!=x[i-1]):
##            tot+=1
##            l=k
##            k=1
##        if(x[i]==x[i-1]):
##            if(k==0 and l==0):
##                tot+=1
        
