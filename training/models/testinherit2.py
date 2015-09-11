from openerp import models,fields,api,_
class Inherit(models.Model):
    _name = 'viewlevel'

    name = fields.Char()
    age=fields.Integer(string='age')
    check=fields.Selection([('single','Single'),('married','Married')])
    regis=fields.Char(string='regist')