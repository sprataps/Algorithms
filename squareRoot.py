def sqrt(val):
    if val==0 or val==1:
        return val
    low=1
    high=val
    while(low<high):
        m=low+(high-low)//2
        print(m)
        if m==val/m:
            return m
        elif m>val/m:
            high=m
        else:
            low=m+1

    return low-1


def sqrtWithPrecision(val,p):
    low=0
    high=val
    while(low<high):
        m=low+(high-low)/2
        if abs(m*m-val)<=p:
            return m
        elif (m*m-val)>p:
            high=m
        else:
            low=m+p
    return low


print(sqrtWithPrecision(20,.001))
