# Function that accepts a list of lists that contain name,age and salary and also accepts a string representing the key to sort by.
# It returns a new list containing the list with each employee sorted in ascending order by key.
# String parameter "sort_by" will always be "name" or "age" or "salary"

def sort_employees(employees,sort_by):
    sort_indices=["name","age","salary"]
    sort_index=sort_indices.index(sort_by)
        
    sorted_emp=[]
    
    def key_giver(employee):
        return employee[sort_index]   
    
    new_employees_list=sorted(employees,key=key_giver)
    return new_employees_list

# learnt the importance of .index() and sorted with key







