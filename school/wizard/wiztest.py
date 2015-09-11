from openerp import models,api,fields,_ 
 
class wiz_form(models.TransientModel):
    _name = 'wiztest'
    
    
    
    name=fields.Char('Name 1')
    pname= fields.Char('Name 2')
    state = fields.Selection([('step1', 'step1'),('step2', 'step2')])  
