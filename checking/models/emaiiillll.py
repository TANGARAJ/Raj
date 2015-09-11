from openerp import models,fields,api,_   
import dateutil
from datetime import datetime 
class whatever(models.Model):
    _name='whatever'
    _rec_name='name'
    
    staffname=fields.Char()
    state=fields.Selection([('draft','Draft'),('sent','Sent'),('closed','Closed')])
    checkaccno=fields.Many2one('check.one','customer_id')
    name=fields.Char('availablebal', size=64, required=True)
    checking=fields.Char('Checking')
    
    @api.onchange('checking')
    def onchange_values(self):
        student_ids = []
        name={}
        if name:
            stud_obj=self.env['check.one']
            check=stud_obj.browse(self.name)
            student_ids=stud_obj.search([('name','=',check.name.name)])
        return {'value':{'checkaccno': student_ids}}
        
    
    
  
#     @api.onchange('custname')
#     def onchange_custname(self):
#       if self.name=self.
#          self.name="check.one","customer_id"
#     
    
    
    
    @api.onchange('checkaccno')
    def onchange_checkaccno(self):
        self.name=self.checkaccno.balance
 
    @api.onchange('state')
    def onchange_state(self):
        if self.state=='draft':
            self.staffname='manager'
            
#     @api.onchange('custname')
#     def onchange_accno(self):
#          self.name=self.custname.accno
#     
    
    
    
    
    
    
#     age=fields.Integer()
#     dob=fields.date('Date of Birth',required=True)
#     age_text=fields.Text('textage')
# 
#     @api.onchange('dob')
#     def onchange_getage_id(self,dob):
#       current_date=datetime.now()
#       current_year=current_date.year
#       birth_date = fields.date(dob)
#       current_age=current_year-birth_date.year
#      val = {
#         'age_text':current_age
#     }
#     return {'value': val}

# @api.onchange()
# def onchange_age(age):
#     # Get the current date
#     now = datetime.datetime.utcnow()
#     now = now.date()
# 
# 
#     age = dateutil.relativedelta.relativedelta(now, date)
#     age = age.years
# 
#     return age


    #these 3 functions are called by the workflow
#     def draft(context=None):
#         self.write('state'='draft')
#         return True
# 
#     def send(self, cr, uid, ids, context=None):
#         self.write(cr, uid, ids, {'state': 'sent'})
#         return True
# 
#     def close(self, cr, uid, ids, context=None):
#         self.write(cr, uid, ids, {'state': 'closed'})
#         return True    

    @api.multi
    def values_checking(self):
        res_ids=self.search([('id','=',self.id)]).ids
        print self.staffname
        print self.checkaccno
#         print 'dis %s'%(self.display_name)
        print self.ids  

