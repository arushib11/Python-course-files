
class Inventory:
    def __init__(self,max_capacity):
        self.max_capacity=max_capacity
        self.items={}
        self.current_inventory_quantity=0

    def add_items(self,name,price,quantity):
        if quantity+self.current_inventory_quantity>self.max_capacity:
            return False
        if name in list(self.items.keys()):
            return False
        self.items[name]={"name":name,"price":price,"quantity":quantity}
        self.current_inventory_quantity+=quantity
        return True
    
    def delete_item(self,name):
        if name not in list(self.items.keys()):
            return False
        self.current_inventory_quantity-=self.items[name]["quantity"]
        del self.items[name]
        return True
    
    def get_most_stocked_item(self):
        t_name=None
        max_quantity=0

        for item in self.items:
            t_name=self.items[item]["name"]
            t_quantity=self.items[item]["quantity"]
            if t_quantity>max_quantity:
                max_quantity=t_quantity
                max_name=t_name
        return max_name


    def get_items_in_price_range(self,min_price,max_price):
        price_range_items=[]
        for item in self.items:
            if item[item]["price"]>=min_price and item[item]["price"]<=max_price:
                price_range_items.append(item)
        return price_range_items

       


'''
dic={"choc":{"name":"choc","price":5.99,"quantity":5},"bread":{"name":"bread","price":2.99,"quantity":3}}
print(list(dic.values()))
price_range_items=[]
for item in dic:
            if dic[item]["price"]>=1 and dic[item]["price"]<=5:
                price_range_items.append(item)
print(price_range_items)
'''
