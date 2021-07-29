
def binary(l,item,min,max):
    left=min
    right=max
    avg=min+(max-min)//2
    if l[avg]>item:
        left,right=min,avg
        return binary(l,item,left,right)
    elif l[avg]<item:
        right,left=max,avg
        return binary(l,item,left,right+1)
    else:
        return '{} is in index {}'.format(l[avg],avg)
print(binary([1,2,3,4,5,6],6,0,4))