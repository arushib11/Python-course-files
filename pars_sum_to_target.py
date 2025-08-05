# A function that accepts two lists of integers and a target integer. Function should return all pairs of indices [x,y]
# where list1[x]+list2[y]==target. List1 and list2 will have same number of elements in anyorder.

#list1=[1,-2,4,5,9]
#list2=[4,2,-4,-4,0]
def pairs_of_indices_func(list1,list2,target):
    pairs_of_indices=[]

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]+list2[j]==target:
                pairs_of_indices.append([i,j])

    return pairs_of_indices

# Learnt to append nested list by .append([i,j])