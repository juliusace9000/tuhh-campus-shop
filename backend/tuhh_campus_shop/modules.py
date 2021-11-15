class ProductQuerySet(models.QuerySet):

    # no need for a constructor
    # Python to SQL

    """+ string: Get_Product_Description(product_ID)"""
    def Get_Product_Description(self, product_ID):
        return self.filter(pk=product_ID).first().product_Description
        
    """+ string: Get_Product_Picture_Path(product_ID)"""
    def Get_Product_Picture_Path(self, product_ID):
        return self.filter(pk=product_ID).first().picture_Path

    # other miro methods...
