from openerp import models, fields, api, _
import time
import logging 
from datetime import datetime 
_logger = logging.getLogger(__name__)
 
class Training(models.Model):
    _name='training.details'


    name=fields.Many2one("res.partner",string='trainee_name',required=True)
    status=fields.Selection([('rajini','rajini'),('kamal','kamal')])
    age=fields.Integer(string='age', required=True,)
    course=fields.Char(string='course')
    fee=fields.Integer(string='course fees',required=True)
#     date=fields.Date(default=datetime.today())
    gender = fields.Selection([('Male', 'Male'),('Female', 'Female')])
    current_time=fields.Char(string="Current Time: ",default=time.strftime('08:00:00'),readonly=True) 
    description=fields.Text() 
    checking_id=fields.Many2many('process','name','abcd')
    process_ids = fields.One2many('process', 'abcd', string="Process")
    gold=fields.Reference([('random.process','random process'),('training.details','training details')])
    date=fields.Datetime('Creation Date', required=True)
     
    _defaults = {
        'date': lambda *a: time.strftime('%Y-%m-%d 02:30:00'),
#         "date":lambda*a: time.strftime(),
    }

    
    
    
#     status=fields.Selection([('rajini','rajini'),('kamal','kamal')])
#     gold=fields.Reference(selection='check_search')
#     _sql_constraints = [
# #         ('name_description_check',
# #          'CHECK(name != description)',
# #          "The title of the course should not be the description"),
# 
#         ('age_unique',
#          'UNIQUE(age)',
#          "The Trainee age already exist "),
#     ]

    @api.model
    def test_scheduler(self):
        _logger.info("Scheduler Testing"+str(datetime.today()))
        return True
    
    def example_method(self, cr, uid, ids, context=None):
        _logger.info("Server Action"+str(datetime.today()))
        return True
    
    @api.multi
    def random(self):
        if self.age==20:
            print 'tangaraj'
    
#     @api.multi
#     def button_method(self):
#         return True
#     
#     
#     
#     
#     @api.onchange('gender')
#     def _onchange_gender(self):
#        self.message = "Dear %s" % (self.gender.name)field
   
#     
#     @api.depends('fee')
#     def change_id(self):
#         self.sum=self.fee+10
         
 
    
    

    @api.multi
    def check_search(self):
        res= self.search([('age','=','20')])
        
#         for record in res:
        self.write({'age': '30'})
             
    



        
#      @api.multi
#     def check_search(self):
#         res = self.search([('selection_field','=','Male')])
#         for record in res:
#             record.write({'created' :'val1'})
#             
#          
#    