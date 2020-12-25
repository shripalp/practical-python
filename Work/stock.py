class stock:
    __slots__ = ( 'name', '_shares', 'price' )
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError ('Expected int')
        self._shares = value
        
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property    
    def cost(self):
        return self.shares * self.price

    @property
    def sell(self, n):
        self.shares = self.shares - n

class mystock(stock):
    def panic(self):
        self.sell(self.shares)
    def cost(self):
        return 1.25 * self.shares * self.price

    



