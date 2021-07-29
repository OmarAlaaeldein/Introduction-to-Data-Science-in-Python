l=[]
no_points,no_segmants=map(int,input().split())
for i in range(no_points):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort(key=lambda a:(a[0],a)
l_segmants=list(map(int,input().split()))
l_occur=[0 for k in range(no_segmants)]
min(intersection hint)
#for j in range(no_segmants):
    #for o in l:
        if l_segmants[j]>=o[0] and l_segmants[j]<=o[1]:
            l_occur[j]+=1
print(*l_occur)

    #sort_list = chain(start_points, end_points, point_points)
 #   sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))