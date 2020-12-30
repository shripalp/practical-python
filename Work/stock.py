class stock:
    __slots__ = ( 'name', '_shares', 'price' ) #attributes cannot be changed or added
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property #creating a function shares
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int): # this function checks the value validation
            raise TypeError ('Expected int')
        self._shares = value
        
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property    #function can be called without ()
    def cost(self):
        return self.shares * self.price

    @property  #function can be called with out ()
    def sell(self, n):
        self.shares = self.shares - n

class mystock(stock): #child class(inheritance) from class stock
    def panic(self):
        self.sell(self.shares)
    def cost(self):
        return 1.25 * self.shares * self.price

    



