# Practicing .sort method and sorted() function

lst=[1,2,3,4,3,2,1,23,3,2,1]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
new_lst=sorted(lst)
print(new_lst)
new_lst=sorted(lst,reverse=True)
print(new_lst)

# Practicing .sort() and sorted() on nested lists

lst=[[1,-2],[3,-4],[5,-6],[-1,-2],[0,0]]
lst.sort()
print(lst) # sorts by the first element only

# rewriting to sort by second element in nested list

def return_second_index(item):
    return item[1]

lst=[[1,-2],[3,-4],[5,-6],[-1,-2],[0,0]]
lst.sort(key=return_second_index)
print(lst)

# rewriting to sort by of of the elements of each nested list

def return_sum_elem(elem):
    return sum(elem)

lst=[[1,-2],[3,-4],[5,-6],[-1,-2],[0,0]]
lst.sort(key=return_sum_elem)
print(lst)

# using sorted() for dictionary

dict_s={"Vis":44,"Nan":12,"ANc":33,"Aru":39}
res=sorted(dict_s,key=dict_s.get)
print(res)
