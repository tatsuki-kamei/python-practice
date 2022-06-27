only3_list=[]
only3_list2=[]
for i in range(1,41):
    if i % 3 == 0:
        for a in str(i):
            if int(a) == 3:
                only3_list.append(i)
                break
print(only3_list)

for i in range(1,41):
    if i %3 ==0 and "3" in str(i):
        only3_list2.append(i)
print(only3_list2)
