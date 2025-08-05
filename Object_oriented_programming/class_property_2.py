class Time:
    def __init__(self,second):
        self._second=second
    
    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self,second):
        if second<0 or second>60:
            raise ValueError("Invalid")
        self._second=second

t=Time(54)
t.second=10
print(t.second)