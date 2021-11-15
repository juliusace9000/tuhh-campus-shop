##### Andrei
class ProductQuerySet(models.QuerySet):

    def Get_Price(self, productID):             
        return self.filter(product_ID=productID).first().price         

    def Get_Product_Stock(self, productID):             
        return self.filter(product_ID=productID).first().product_Stock    
#####

##### Yossef
    def Get_Product_Description(self, productID):
        return self.filter(product_ID=productID).first().product_Description
        
    def Get_Product_Picture_Path(self, productID):
        return self.filter(product_ID=productID).first().picture_Path 
#####


# don't forget productQueryManager = ProductQuerySet.as_manager()   


    






