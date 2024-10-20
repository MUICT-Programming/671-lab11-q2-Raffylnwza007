n = int(input())
lst1=[]
lst2=[]

for i in range(n):
    lst1.append(int(input()))
for i in range(n):
    lst2.append(int(input()))

def summation(lis1, lis2):
    updated_list = []
    for i in range(n):
        updated_list.append(lis1[i] + lis2[i])
    return updated_list

def find_min_max(lis):
    return min(lis), max(lis)

sum = summation(lst1, lst2)
rst = find_min_max(sum)

print(sum)
print(rst)
