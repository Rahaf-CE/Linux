class Product:
    numOfProducts=0
    def __init__(self,Product_id,Product_name,Product_category,Price,Inventory,Supplier,Has_an_offer,Offer_Price,valid_Until):
        self.Product_name=Product_name
        self.Product_id=Product_id
        self.Product_category=Product_category
        self.Price=Price
        self.Inventory=Inventory
        self.Supplier=Supplier
        self.Has_an_offer=Has_an_offer
        self.Offer_Price=Offer_Price
        self.valid_Until=valid_Until

        Product.numOfProducts+=1
