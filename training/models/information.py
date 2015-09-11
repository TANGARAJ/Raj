from openerp import models, fields, api, _
from datetime import datetime 
import time 


# def selection_name(self):
#     return [('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel', 'Cancel'), ('done', 'Done')]
#    
       
class questions_load(models.Model):
     
    
    _name="process"
    _description="Load sample questions"
   
    
#     name=fields.Char(string="Trainee name")
    current_time=fields.Char(string="Current Time: ",default=time.strftime('%I:%M:%S'),readonly=True)
    abcd=fields.Many2one('training.details',string='Trainee name',required=True)
    trainer=fields.Many2one('random.process',string='Trainer name')
    qns1=fields.Text(string="Duration:",readonly=True,default="Click next to see duration!")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel', 'Cancel'), ('done', 'Done')], default='draft')
    training_ids=fields.Many2many('training.details', string="Training")
#     selection_field = fields.Selection(selection=selection_name)
    process_ids = fields.One2many('training.details', 'name',string="Process")
    status=fields.Selection([('rajini','rajini'),('kamal','kamal')])
    
    
    anss1234=fields.Text(string="Batch timing:")

    list1=["6 month",'3 month',
           "12 month","18 month",
           "2 month",
           "4 weeks",
           "2 years"]
    
    list2=["6 a.m to 9 a.m",'3 month',
           "12 month","18 month",
           "2 month",
           "4 weeks",
           "2 years"]
    
    
 
    i=0
    j=0
    @api.one 
    def load_questions(self):
        global i
     
        if(questions_load.i<len(self.list1)):
            self.qns1=self.list1[questions_load.i]
            questions_load.i=questions_load.i+1
#             print questions_load.i
        else:
            self.qns1="END OF THE QUESTIONS!"
            questions_load.i=0
                          
    
    
#     @api.onchange('abcd')
#     def onchange_next(self):
#         rec=self.env['training.details'].search([('name','=',self.abcd.name)]).status
#         self.status=rec.status
        
    @api.one 
    def make_confirm(self):
        self.state = 'confirm'
       
        self.create({'qns1':'whts ur name?','anss1234':'Tangaraj'}) 
         
    @api.one
    def batch_time(self):
        if(questions_load.j<len(self.list2)):
            self.anss1234=self.list2[questions_load.j]
            questions_load.j=questions_load.j+1
#             print questions_load.j
    @api.multi
    def searching_checking(self):
        res=self.search([('qns1','=','2 month')])    
        for record in res:
            record.write({'qns1':'24 month'})
            
            
            
    @api.onchange('abcd')
    def onetwomany(self):
        if self.abcd:
            line1={'name':'tangaraj','age':'100','fee':'5000'}
            line2={'name':'atchuthan','age':'22','fee':'50514'}
            line3={'name':'dhinesh','age':'32','fee':'5000'}
            self.process_ids=[(0,0,line1),(0,0,line2),(0,0,line3)]   
             
#     @api.multi
#     def name_checking(self):
#         res_ids=self.browse([1,2,3])
# #         print self.env['subject.details'].browse(res_ids)
#         print res_ids
    @api.multi
    def name_checking(self):
        res_ids=self.search_count([('qns1','=','24 month')])
#         self.env.ref('Training_form')
#         print self.env['subject.details'].browse(res_ids)
        print res_ids   
         
#     @api.multi
#     def onchange_next(self):
# #         res= self.env['subject.details'].search([('enrolment_number','=',self.enrolment_number)])
#         rec=self.env['training.details'].search([('name','=',self.name)])
#         self.status=rec.status
#         print rec     
               
class sample_process(models.Model):           
    _name='sample'
    _inherit="process"
     
     
    check_name=fields.Many2one('training.details','name')
#     status=fields.Selection([('rajini','rajini'),('kamal','kamal')])
#     
    
#     @api.onchange('check_name')
#     def onchange_next(self):
# #         res= self.env['subject.details'].search([('enrolment_number','=',self.enrolment_number)])
#         rec=self.env['training.details'].search([('name','=',self.check_name)])
#         self.status=rec.status
#         print rec     
        
        
    
#     
#     @api.multi
#     def name_checking(self):
#         res_ids=self.env['process'].search_read([],['abcd'])
# #         print self.env['subject.details'].browse(res_ids)
#         print self.abcd
    
#     @api.multi
#     def name_checking(self):
#         res=self.search(['id','=',self.id]).ids 
#         print self.ids
                        