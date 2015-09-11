from openerp import models,fields,api,_
from openerp.exceptions import Warning, ValidationError

 
class constraints(models.Model):
    _name = 'constraints'

    name=fields.Char()     
    age=fields.Integer()
    password=fields.Char()
    
#     
# 
#     @api.onchange('age')
#     def onchange_age(self):
#         if self.age >= 100:
#             self.age=0
# #             raise ValidationError(_('Age cannot be greater than 100'))
#             return {'warning':{
#                                'title': 'Warning',
#                                'message': 'Age canram11111111111not be greater than 100'
#                                }}
#   @api.depends   
    @api.one
    @api.constrains('age')
    def _check_const(self):
        if self.age>100:
            raise ValidationError("too old is not allowed")
           
#         
        
        
        
#     @api.one
#     @api.constrains('password')f
#     def _check_instructor_not_in_password(self):
#         if not isinstance(self.name, int):
#             raise ValidationError("password only contain string")
#  
#  