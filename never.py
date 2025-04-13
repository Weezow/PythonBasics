class InvManager:
    def __init__(self):
        self.inventory = {"apples" : 12, "bananas" : 9}
        
    def lookproduct(self, product):
        for item in self.inventory:
            print(item)
            if item["product"] == product:
                print("product")

inventory = InvManager()
inventory.lookproduct("product")




    #def stock(self, product, amount):


    #def out_of_stock(self, product, amount):
    

    #def import_product(self, product, amount):