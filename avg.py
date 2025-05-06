num=[-7,-2,-1,-5,1,2,3,4]
pos_num=[]
neg_num=[]
for i in num:
    if i< 0:
        neg_num.append(i)
    else:
        pos_num.append(i)
print("average of pos:",sum(pos_num)//len(pos_num))
print("average of neg:",sum(neg_num)//len(neg_num))