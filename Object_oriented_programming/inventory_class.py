'''
Write an Inventory class that handles inventory management of a company. 
All instances are initialized by passing max_capacity that indicates the max no. of items that can be stored in invetory
Invetory class needs to store items represented by name,price and quantity. Class implements:
add_item(name,price,quantity): adds item to inventory and returns True. If adding results in exceeding capacity or the name passed already exists in inventory, return False and don't add.
delete_item(name): deletes item and returns True. If item with passed name doesn't exist, return False
get_most_stocked_item(): returns name of item with highest quantity and None if no item in invetory. Assume it will be only one item
get_items_in_price_range(min_price,max_price): Returns list of names of items that have price in the range(inclusively)
'''

class Inventory:
    def __init__(self,max_capacity):
        self.max_capacity=max_capacity
        self.items={}
        self.count=0

    def add_item(self,name,price,quantity):
        if name in self.items:
            return False

        if self.count+quantity>self.max_capacity:
            return False


        self.items[name]={"name":name,"price":price,"quantity":quantity}
        self.count+=quantity     # need to remember to increase the count
        return True
    
    def delete_item(self,name):
        if name not in self.items:
            return False
        self.count-=self.items[name]["quantity"]  # need to do this first before deleting
        del self.items[name]
        return True

    def get_most_stocked_item(self):

        most_stocked_item_name=None
        largest_quantity=0

        for elem in self.items:
            name=self.items[elem]["name"]
            quantity=self.items[elem]["quantity"]
            if quantity>largest_quantity:
                most_stocked_item_name=name
                largest_quantity=quantity
        return most_stocked_item_name
        

    def get_items_in_price_range(self,min_price,max_price):
        price_range_list=[]
        for elem in self.items:
            if self.items[elem]["price"]<=max_price and self.items[elem]["price"]>=min_price:
                price_range_list.append(elem)
        return price_range_list


inventory=Inventory(4)
print(inventory.add_item('Chocolate', 4.99, 1))
print(inventory.add_item('Cereal', 6.99, 1))
print(inventory.add_item('Milk', 3.99, 2))
print(inventory.add_item('Butter', 2.99, 1))
print(inventory.delete_item('Bread'))
print(inventory.delete_item('Cereal'))
print(inventory.get_items_in_price_range(4.50,6.50))

'''
different things I tried

print(inventory.add_item('Chocolate', 4.99, 2))
print(inventory.add_item('Bread', 4.99, 2))
print(inventory.get_most_stocked_item()) 
#print(inventory.add_item('Butter', 4.99, 1))
#print(inventory.add_item('Bread', 4.99, 2))
#print(inventory.get_most_stocked_item())

smaller program that I ran to understand how nested dictionaries behave

items={}
def items_list(name,price,quantity):
    items[name]={"name":name,"price":price,"quantity":quantity}
    return items
items_list("bread",2.5,3)
items_list("milk",5.99,1)
items_list("eggs",9.99,2)
print(items,"\n")
print(items["bread"])
print(items["bread"]["price"])
print(items["bread"]["quantity"])

def get_items_in_price_range(min_price,max_price):
        price_range_list=[]
        for elem in items:
            if items[elem]["price"]<=max_price and items[elem]["price"]>=min_price:
                price_range_list.append(elem)
        return price_range_list
p=get_items_in_price_range(3,10)
print(p)

lst=[]
for elem in items:
    lst.append(items[elem]["quantity"])
x=max(lst)
print(x)'''
