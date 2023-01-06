file=open('exam_02.txt','r') #here input is txt file with lines are seperated by enter and words are seperated by spaces
docs=file.read().split('\n')
dataset=list()
for i in docs:
    dataset.append(i.lower().split(' '))
print(dataset)
print('---------'+'\n'+'------')
uniquewords=list()
for i in dataset:
    for j in i:
        uniquewords.append(j)
uniquewords=list(set(uniquewords))
print(uniquewords)

def frequency(x,l):
    count=0
    for i in l:
        if(i==x):
            count+=1
    return count
dataset_c=list()
for i in dataset:
    l_temp=list()
    for j in uniquewords:
        temp=frequency(j,i)
        l_temp.append(temp)
    dataset_c.append(l_temp)
print('-------'+'\n'+'--------')
print(dataset_c)
def cosinesim(l1,l2):
    sum=0
    for i,j in zip(l1,l2):
        sum=sum+i*j
    l1sqr=0
    l2sqr=0
    for i in range(len(l1)):
        l1sqr=l1sqr+(l1[i])**2
        l2sqr=l2sqr+(l2[i])**2
    return sum/((l1sqr**0.5)*(l2sqr**0.5))
print('-------'+'\n'+'--------')
cosinesim_mat=list()
for i in dataset_c:
    cos=list()
    for j in dataset_c:
        cos.append(cosinesim(i,j))
    cosinesim_mat.append(cos)
for i in range(len(cosinesim_mat)):
    print('\n')
    for j in range(len(cosinesim_mat)):
        print(cosinesim_mat[j])