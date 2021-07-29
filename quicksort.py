import random
import statistics
def p3(low,high,l):
    k=l[low]
    s=low+1
    e=low
    for i in range(low+1,high+1):
        if l[i]<=k:
            e+=1
            l[i],l[e]=l[e],l[i]        
            if l[e]<k:
                l[s], l[e] = l[e], l[s]
                s += 1
    l[low],l[s-1]=l[s-1],l[low]
    return [s,e]
def qs(low,high,l):
    if low>=high:
        return
    p=statistics.mode(l[low:high+1])
    l[low],l[p]=l[p],l[p]
    [p1,p2]=p3(low,high,l)
    qs(low,p1-1,l)
    qs(p2+1,high,l)
n=int(input())
l=list(map(int,input().split()))
qs(0,len(l)-1,l)
print(*l)