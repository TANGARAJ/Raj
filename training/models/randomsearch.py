from openerp import models, fields, api, _
import time
import logging 
from datetime import datetime 
_logger = logging.getLogger(__name__)
class random_sdhfusdfhsdf(models.Model):
    _name="random.process"
    _table_name = "random_sdhfusdfhsdf"
    _description="Load sample questions"
    _rec_name="trainer"
  
     
    trainer=fields.Char(string='Trainername')
    name=fields.Char(string='NAME OF THE COURSE')
    rqns123=fields.Char(string="QUALIFICATION: ",required=True)
    rans123=fields.Text(string='Details about Trainer: ')
    date=fields.Date(default=datetime.today())

#     new123=fields.Char()
    listqns=["1","2","3","4"]
    

    @api.multi
    def qns_1(self):
        self.rqns123=self.listqns[0]
          
     
    def example_method(self, cr, uid, ids, context=None):
        _logger.info("Server Action"+str(datetime.today()))
        return True      
          
            
#     def qns_1(self):
#         self=self.listqns[0]
#         @api.multi