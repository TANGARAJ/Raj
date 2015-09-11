from openerp import models,fields,api,_
class delegation(models.Model):
    _name = 'delegation_base'
    _inherits={'child1':'id1','child2':'id2','child3':'id3'}

    name = fields.Char(required=True)
    age=fields.Integer(string='age')

    id1=fields.Many2one('child1',required=True,ondelete='cascade')
    id2=fields.Many2one('child2',required=True,ondelete='cascade')
    id3=fields.Many2one('child3',required=True,ondelete='cascade')
    
    

class child1(models.Model):
    _name = 'child1'


    call=fields.Char(string="register")
        
    

class child2(models.Model):
    _name = 'child2'

    calling=fields.Char(string="Division")
    
class child3(models.Model):
    _name = 'child3'


    chart=fields.Char(string="Year")
    
    