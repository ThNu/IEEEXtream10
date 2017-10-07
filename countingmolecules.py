c,h,o=map(int,raw_input().split())

if h==0:
    if (2*c==o):
        print 0,c,0
    else:
        print "Error"

elif o==0:
    if c==0 and h==0:
        print 0,0,0
    if c!=0 or h!=0:
        print "Error"

elif c==0:
    if h=2*o:
        print o,0,0
    else:
        print "Error"

else:
    if c<6:
        if o<2*c:
            print "Error"
        else:
            O=o-2*c
            if h!=2*O:
                print "Error"
            else:
                print O,c,0
    if c>=6:
        co2=(2*o-h)/4.0
        c6h12o6=(4*c+h-2*o)/24.0
        h2o=(2*o+h-4*c)/4.0

        if(co2%1!=0 or c6h12o6%1!0 or h2o%1!=0):
            print "Error"
        else: print co2,c6h12o6,h2o
        
            
        
    
