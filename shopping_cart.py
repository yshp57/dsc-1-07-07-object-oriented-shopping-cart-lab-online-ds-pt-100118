class ShoppingCart:
    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
    def get_total(self):
        return self._total
    def set_total(self, number):
        self._total = number
    total = property(get_total, set_total) 
    
    def get_items(self):
        return self._items
    def set_items(self, list):
        self._items = list
    items = property(get_items, set_items)
    
    def get_employee_discount(self):
        return self._employee_discount
    def set_employee_discount(self, number):
        self._employee_discount = number
    employee_discount = property(get_employee_discount, set_employee_discount)
    
    def add_item(self, name, price, quantity = 1):
        for i in range(0, quantity):
            self.items.append((name,price))
            self.total += price
        return self.total
    
    def mean_item_price(self):
        return (self.total)/(len(self.items))
    
    def median_item_price(self):
        pricelist = []
        for item in self.items:
            pricelist.append(item[1])
        pricelist = sorted(pricelist)
        if len(pricelist)%2 == 0:
            median = pricelist[(int((len(pricelist)/2)))]+pricelist[int(((len(pricelist)/2)+1)/2)]
        else:
            median = pricelist[int((len(pricelist)/2)+.5)]
        return median
    def apply_discount(self):
        if self.employee_discount:
            return ((self.total)*((100-(self.employee_discount))/100))
        else:
            return "Sorry, there is no discount to apply to your cart :("
    def item_names(self):
        return [i[0] for i in self.items]
    def void_last_item(self):
        if self.items:
            self.total -= self.items[-1][1]
            self.items.pop(-1)
        else:
            return "There are no items in your cart!"
            