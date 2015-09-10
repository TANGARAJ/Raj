from openerp import models,fields,api,_ 
class salesreq(models.Model):
    _name="supermarket"
    
    customer=fields.Char()
    product_name=fields.Char(string="product details")

    @api.multi
    def my_method(self):
        res_ids=self.search([('id','=',self.id)]).ids
        print self.ids, 'tangaraj'
        print self.id


# @api.one 
# def salesvv_reqss(self):
#     
#     global i
#  
#     if(salesreq.i<len(self.list1)):
#         self.product_name=self.list1[salesreq.i]
#         salesreq.i=salesreq.i+1
#         print salesreq.i
#     else:
#         self.product_name="Selection is over!"
#         salesreq.i=0
        
        
        
#     
#     list1=["LUX SOAP",'life boy',
#            "liril","nature power",
#            "cinthol",
#            "hamam",
#            "pears"]
#     
#     
#     i=0
# 

        
                          