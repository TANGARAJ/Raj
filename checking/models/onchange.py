from openerp import fields,models,api,_ 

class onchange_checking(models.Model):
    _name='onchange.checking'
    _rec_name='name'
    
    
    name=fields.Many2one('whatever')
    
    
#     @api.onchange()
#     def onchange_onchange(self):
#         ra=[]
#         if ra in self.name:
#             