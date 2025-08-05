class BankAccount:
    def __init__(self,name):
        self.name=name
        self._balance=0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self,balance):
        if type(balance) not in [int,float]:
            #raise Exception("Please enter a digit")
            return
        if balance<0 or balance>100000:
        # raise Exception("The balance cannot be less than 0 or more than 100000")
            return
        self._balance=balance


    
    #balance=property(getattr,set_balance)
    
#int and float don't have isdigit(), so we use 'in' operator to check for digit validity
        


    
