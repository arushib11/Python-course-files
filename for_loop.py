# Using single for loop to print elements that are both divisible by 2 and located at an odd index

lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

for i in range(len(lst)):
    if i%2==1 and lst[i]%2==0:
        print(lst[i])
print("#####")

#Using nested for loop to print respective sums of the  inner list, each on a separate line
lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]
for i in range(len(lst)):
    sum=0
    for j in range(len(lst[i])):
        sum=sum+lst[i][j]
    print(sum)
print("#####")
# Use single for loop to iterate through list of numbers, and for each number,print sum of number and one to it's right
st = [-2, 0, 4, 5, 1, 2]
for i in range(len(st)-1):
    sum=st[i]+st[i+1]
    print(sum)