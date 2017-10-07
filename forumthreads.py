
while(True):

    a,p=map(int,raw_input().split())
    thred=[]
    postno=0
    for a0 in xrange(p):
        x=input()
        postno+=1
        if x==0:
            thred.append([postno,1])
        else:
            for element in thred:
                if x==element[0]:
                    element[1]+=1
                    element[0]=postno
    array=[]
    length=0
    for element in thred:
        array.append(abs(element[1]-3))
        length+=1
    print min(array)
        
    

##    n=0
##    maxi=-1
##    while(n<length):
##        sum =0
##        while(n<length):
##            sum+=array[n]
##            if sum<3:
##                n+=1
##            elif sum==3:
##                n+=1
##                if maxi<abs(sum-3):
##                    maxi = abs(sum-3)
##                break
##            else:
##                if (sum-3)<=3-(sum-array[n]):
##                    if maxi<abs(sum-3):
##                        maxi = abs(sum-3)
##                    n+=1
##                    break
##                else:
##                    break
##    if maxi<abs(sum-3):
##        maxi = abs(sum-3)
##    print maxi
                

