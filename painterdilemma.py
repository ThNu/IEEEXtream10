t=input()

for a0 in xrange(t):
    n = input()
    paints=map(int,raw_input().split())

    lst={}
    for i in xrange(n):
        item=paints[i]
        if item not in lst:
            lst[item]=[i]
        else:
            lst[item].append(i)

    b1=paints[0]
    lst.get(b1).remove(0)
    b2=-1
    count=1;
    for i in range(1,n):
        item=paints[i]
        if(b2==-1):
            if(b1!=item):
                b2=item
                count+=1
                lst.get(b2).remove(i)
            else:
                lst.get(b1).remove(i)
                
        elif(lst[b1]==[]):
            if(b2!=item):
                b1=item
                count+=1
                lst.get(b1).remove(i)
            else:
                lst.get(b2).remove(i)
            
        elif(lst[b2]==[]):
            if(b1!=item):
                b2=item
                count+=1
                lst.get(b2).remove(i)
            else:
                lst.get(b1).remove(i)

        else:
            if(item!=b1 and item!=b2):
                if(lst[b1][0]<lst[b2][0]):
                    b2=item
                    count+=1
                    lst.get(b2).remove(i)
                else:
                    b1=item
                    count+=1
                    lst.get(b1).remove(i)
            else:
                if(item==b1):
                    lst.get(b1).remove(i)
                else:
                    lst.get(b2).remove(i)

    print count

        

    
