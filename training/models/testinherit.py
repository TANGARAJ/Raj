from openerp import models,fields,api,_
class Inheritance0(models.Model):
    _name = 'inheritance.0'

    name = fields.Char()
    age=fields.Integer(string='age')
    regis=fields.Char(string='regist')
 
    
    
    
    

class Inheritance1(models.Model):
    _name = 'inheritance.1'
    _inherit = 'inheritance.0'

    call=fields.Char(string="register")
    
    