from models import *
import operator
group_dict={}



for group in Group.select():
    join_groups = JoinGroups.filter(group=group)
    users=[]
    for join_group in join_groups:
        users.append(join_group.user)

    group_dict[group.name]=len(users)

sorted_freq_tuple=sorted(group_dict.items(),key=operator.itemgetter(1))
print(sorted_freq_tuple)
reversed_sorted_freq_tuple=list(reversed(sorted_freq_tuple))
print(reversed_sorted_freq_tuple)

file = open('testfile3.txt', 'w')

for tuple in reversed_sorted_freq_tuple:
    file.write(str(tuple[0])+ ', '+str(tuple[1])+'\n')
    print(tuple)

file.close()
