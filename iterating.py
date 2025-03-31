# d = {"key" : "value"}
# l = [1,2,3,4,5,6]
# print(d["key"])

# for key, value in d.items():
#     print(key)
#     print(value)

ld = [
        {"product":"apples","quantity":10},
        {"product":"bananas","quantity":12},
        {"product":"peaches","quantity":8},
    ]

# In list associate the value to variable for each item in that list

for poop in ld:
    # print(item)
    print(poop["product"])

# def f(param):
#     return 

class InvManagement:
    def __init__(self):
        self.inventory = {"apples": 12 , "bananas" : 10}
    
    def lookup(self, product):
        for stock in self.inventory:
            if stock == product:
                print(stock)
                print(self.inventory[stock])

i = InvManagement()
i.lookup("bananas")