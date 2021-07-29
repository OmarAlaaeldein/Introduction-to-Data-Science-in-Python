n1=int(input())
s1=list(map(int,input().split()))
n2=int(input())
s2=list(map(int,input().split()))
c,index=0,0
for i in range(max(n1,n2)):
    if len(s1)>=len(s2):
        if s1[i] in s2[index::]:
            c+=1
            index+=s2.index(s1[index])
    elif len(s2)>len(s1):
        if s2[i] in s1[index::]:
            c+=1
            index+=s1.index(s2[index])
print(c)
    