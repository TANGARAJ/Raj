from openerp import models,fields,api,_

class sample(models.Model):
    
    _name='comp'
    
   
    n1=fields.Float()
    name=fields.Text(string="Computing", readonly=True)
    n2=fields.Float(string='cal')

    sum=fields.Float(compute='comp_id',string='answer')
#     total=fields.Float()
    
    @api.depends('n1','n2')
    def comp_id(self):
        self.sum=self.n1+self.n2+10
        
        
#         self.total=self.sum
#     
#     @api.onchange('n1', 'n2') # if these fields are changed, call method
#     def check_change(self):
#        if self.n1 < self.n2:
#            self.n3 = True
# @api.depends('n1','n2','newmodule.lastname')
#     def comp_id(self):
#         self.sum=self.n1+self.n2+10