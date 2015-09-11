from openerp import models, fields, api, _
from openerp.exceptions import Warning, ValidationError
import datetime
import random
import time
from apt.package import Record
from pprint import pprint
from datetime import datetime
from dateutil import parser
# class account_voucher(models.Model): 
#     _inherit="account.voucher"
#     
#     @api.multi
#     def onchange_journal(self, journal_id, line_ids, tax_id, partner_id, date, amount, ttype, company_id):
#         res = super(account_voucher, self).onchange_journal(journal_id, line_ids, tax_id, partner_id, date, amount, ttype, company_id)
#         print res
#         
#     @api.model
#     @api.multi
#     def name_get(self):
#         
#         result = self.env['account.voucher'].search(['id','=',self.id]).ids
# #         for record in self.browse(self.ids):
#         self.ids = str(self.name) + " " + str(self.reference)
#         print result.items()
#         return result.items()  
   
#     @api.multi
# #     @api.depends(lambda self:(self._rec_name, ) if self._rec_name else ())
#     def _display_name(self):
# #         models.Model._compute_display_name(self)(self):
#         
#         result = {}
#         for record in self.browse(self.ids):
#             result[record.id] = str(record.name) + " " + str(record.reference)
#         print result.items()
#         return result.items()
    
#     
#     @api.one
#     @api.depends('onemany')
#     def  _display_name_compute(self): 
#         res=[]
#         for partner in self:
#             res[partner.id]=str(partner.name) + " " + str(partner.reference)
#             print res.items()
#         <<operation on context... you need to check yourself>>
#         <<you will have to check how name_get is called and based on  
#              the return value set the value as shown below>>
#         partner.display_name = <<returned value from name_get>>
 
#         display_name = fields.Char(compute="_display_name",string="Display Name")




class newmodules(models.Model):
    _name = 'newmodule'
    _rec_name="display_name"
    
    _sql_constraints = [('unique_name', 'unique(name)', 'A record with the same name already exists.')]
    
    name = fields.Many2one("enrolment")
    lastname=fields.Char()
    due_amount = fields.Char()
    rare=fields.Char()
    cust_id = fields.Integer(required=True) 
    select=fields.Selection([('area1','area1'),('area2','area2')])
    onemany=fields.Many2one('account.voucher')
    recordcke=fields.Selection([('change','change'),('rere','rere')])
    tname = fields.Html()
    hghf=fields.Char(string="hai")
    display_name = fields.Char( string='Display Name', compute='_compute_display_name' ) 
    share=fields.Selection([('like','LIke'),('Sign','sign')])
    dob=fields.Date()
    age=fields.Integer()
    state_id=fields.Many2one('res.country.state')
    country_id=fields.Many2one('res.country')
    
    
    @api.onchange('name')
    def onchange_valueseee(self):
        student_ids = []
        name={}
        if name:
            stud_obj=self.env['enrolment']
            check=stud_obj.browse(self.name)
            student_ids=stud_obj.search([('name','=',check.name.name)])
        return {'value':{'checkaccno': student_ids}}
    
    
    @api.model
    def new_method(self):
        result = self.env['newmodule'].search(['id','=',self.id]).ids
        print result
        
    @api.onchange('state_id')
    def onchange_state(self):
        if self.state_id:
            self.country_id=self.state_id.country_id.id
           
#     @api.multi()
#     def checking_context(self):
#         
#         env['res.partner'].sudo
#         env['res.partner'].with_context(onemany=name).find_or_create(name)
#     
#     @api.one 
#     @api.depends('lastname', 'rare')
#     def _compute_display_name(self): 
# #         names = [self.lastname, self.rare] 
#         self.display_name = 'test'
#         print self.display_name
#         
#     
#     
#     
#     
#     
# #     display_name = fields.Char(compute="_display_name",string="Display Name")
# #     ids = fields.Text()
#     
#     @api.onchange('recordcke')
#     def compute_name(self):
#         if self.recordcke=='rere':
#             self.write({'rare':500})

    @api.onchange('recordcke')
    def checking_onchange(self):
        pprint('rare')
        if self.recordcke == "change":
            self.rare=1505050
        else:
            self.rare=' '
            
### IMPORTANT
            
    @api.onchange('share','name')
    def onchange_test(self):
        enrol_obj=self.env['enrolment'].search([('name',"=",self.name.name)])
        if self.name:
            self.share=enrol_obj.share
            
    @api.onchange('dob','age')         
    def onchange_getage_id(self):
        
        dob=self.dob
        if dob:
            current_date=datetime.now()
            current_year=current_date.year
            birth_date = parser.parse(dob)
            current_age=current_year-birth_date.year
            self.age=current_age
       
    @api.onchange('select')
    def onchange_values(self):
        if self.select=="area1":
            self.due_amount=1000   
        if self.select=="area2":
            self.due_amount=6000
#         print(time.time())                 
    @api.one
    def room_method(self):
        res=self.name+"raj"       
        res = ''.join(['Sec_', res])
        self.lastname=res
#         res=self.due_amount+"2000"
#         res=self.lastname=self.name
        print res
    @api.multi
    def result_search(self):
        res_ids=self.search([('id','=',self.id)]).ids
#         print 'dis %s'%(self.display_name)
        print self.ids     
    
    @api.onchange('cust_id','due_amount')
    def onchange_cust_id(self):
        if self.cust_id == 56:
            self.hghf = "dsfff"
        else:
            self.hghf = " "  
            
            
    @api.multi
    def check_search(self):
    
        res= self.env['subject.details'].search([('enrolment_number','=',self.enrolment_number)])
        self.find_rollno=res.enrolment_number
        self.find_name=res.name.name
        self.m1=res.s1_tamil
        self.m2=res.s2_english
        self.m3=res.s3_maths
        self.m4=res.s4_science
        self.m5=res.s5_social
        self.grade=res.grade
        self.total=res.total
        self.result=res.status
        
#         if  self.due_amount >=1000:
#             raise Warning('Warning the due amount is greater than 1000')
        
        
# # class res_partner_extention(models.Model):
# #     _inherit = 'res.partner'
#     
#     
# #         result = {}
# #         for partner in self.browse(cr,uid,ids,context=context):
# #             result[partner.application_number] = partner.enrolment_number + " " + partner.standard
# #         print result.item()
# #         return result.items()  
# #     
#     from openerp import models, fields, api, _
# from openerp.exceptions import Warning, ValidationError
# import datetime
# import random
# import time
# from apt.package import Record
# from pprint import pprint
# 
# # class account_voucher(models.Model): 
# #     _inherit="account.voucher"
# #     
# #     @api.multi
# #     def onchange_journal(self, journal_id, line_ids, tax_id, partner_id, date, amount, ttype, company_id):
# #         res = super(account_voucher, self).onchange_journal(journal_id, line_ids, tax_id, partner_id, date, amount, ttype, company_id)
# #         print res
# #         
# #     @api.model
# #     @api.multi
# #     def name_get(self):
# #         
# #         result = self.env['account.voucher'].search(['id','=',self.id]).ids
# # #         for record in self.browse(self.ids):
# #         self.ids = str(self.name) + " " + str(self.reference)
# #         print result.items()
# #         return result.items()  
#    
# #     @api.multi
# # #     @api.depends(lambda self:(self._rec_name, ) if self._rec_name else ())
# #     def _display_name(self):
# # #         models.Model._compute_display_name(self)(self):
# #         
# #         result = {}
# #         for record in self.browse(self.ids):
# #             result[record.id] = str(record.name) + " " + str(record.reference)
# #         print result.items()
# #         return result.items()
#     
# #     
# #     @api.one
# #     @api.depends('onemany')
# #     def  _display_name_compute(self): 
# #         res=[]
# #         for partner in self:
# #             res[partner.id]=str(partner.name) + " " + str(partner.reference)
# #             print res.items()
# #         <<operation on context... you need to check yourself>>
# #         <<you will have to check how name_get is called and based on  
# #              the return value set the value as shown below>>
# #         partner.display_name = <<returned value from name_get>>
#  
# #         display_name = fields.Char(compute="_display_name",string="Display Name")
# 
# 
# 
# 
# class newmodules(models.Model):
#     _name = 'newmodule'
#     _rec_name="display_name"
#     
#     _sql_constraints = [('unique_name', 'unique(name)', 'A record with the same name already exists.')]
#     name = fields.Char(required=True, string="customer name")
#     lastname=fields.Char()
#     due_amount = fields.Char()
#     rare=fields.Char()
#     cust_id = fields.Integer(required=True) 
#     select=fields.Selection([('area1','area1'),('area2','area2')])
#     onemany=fields.Many2one('account.voucher')
#     recordcke=fields.Selection([('change','change'),('rere','rere')])
#     tname = fields.Html()
#     hghf=fields.Char(string="hai")
#     aaaaa=fields.Char(string="aaaaa")
#     display_name = fields.Char( string='Display Name', compute='_compute_display_name' ) 
#     
# #     @api.one 
# #     @api.depends('lastname', 'rare')
# #     def _compute_display_name(self): 
# # #         names = [self.lastname, self.rare] 
# #         self.display_name = 'test'
# #         print self.display_name
# #         
# #     
# #     
# #     
# #     
# #     
# # #     display_name = fields.Char(compute="_display_name",string="Display Name")
# # #     ids = fields.Text()
# #     
# #     @api.onchange('recordcke')
# #     def compute_name(self):
# #         if self.recordcke=='rere':
# #             self.write({'rare':500})
# 
#     @api.onchange('recordcke')
#     def checking_onchange(self):
#         pprint('rare')
#         if self.recordcke == "change":
#             self.rare=1505050
#         else:
#             self.rare=' '
#             
#              
#              
#           
# #    
# #         
# # 
# # #     @api.multi
# # #     def name_get(self):
# # #         
# # #         result = {}
# # #         for record in self.browse(self.ids):
# # #             result[record.id] = str(record.name) + " " + str(record.lastname)
# # #         print result.items()
# # #         return result.items()
# # #     def name_get(self):
# # #         res=self.env['res.partner'].search(['id','=',self.id]).ids
# # #         print self.ids
# #  
#     @api.constrains('cust_id')
#     def _check_something(self):
#    
#         if self.cust_id <=0:
#           
#             raise Warning("Your record is too gfgfdgold: %s" )  
# #         
# #         
# #         
#     @api.onchange('select')
#     def onchange_values(self):
#         if self.select=="area1":
#             self.due_amount=1000   
#         if self.select=="area2":
#             self.due_amount=6000
# # #         print(time.time()) 
#             self.due_amount=                
#     @api.one
#     def room_method(self):
# #         
#         res=self.search([('name','=',self.name)]).name
# #         for r in res:
#         res=self.name+"raj"       
#         res = ''.join(['Sec_', res])
#         self.lastname=res
# #         res=self.due_amount+"2000"
# #         res=self.lastname=self.name
#         print res
#     @api.multi
#     def result_search(self):
#         res_ids=self.search([('id','=',self.id)]).ids
#         print 'dis %s'%(self.display_name)
#         print self.ids     
#     
#     @api.onchange('cust_id','due_amount')
#     def onchange_cust_id(self):
#         if self.cust_id == 56:
#             self.hghf = "dsfff"
#         else:
#             self.hghf = " "  
#         if  self.due_amount >=1000:
#             raise Warning('Warning the due amount is greater than 1000')
#         
#         
# # # class res_partner_extention(models.Model):
# # #     _inherit = 'res.partner'
# #     
# #     
# # #         result = {}
# # #         for partner in self.browse(cr,uid,ids,context=context):
# # #             result[partner.application_number] = partner.enrolment_number + " " + partner.standard
# # #         print result.item()
# # #         return result.items()  
# class selection(models.Model):
#     _inherit='newmodule'
#     
#     share=fields.Selection_add([('sas','ss'),('Sigssn','sissssn')])
       
# #     @api.multi
# #     def name_get(self):
# #         
# #         result = {}
# #         for record in self.browse(self.ids):
# #             result[record.id] = str(record.name) + " " + str(record.lastname)
# #         print result.items()
# #         return result.items()
# #     def name_get(self):
# #         res=self.env['res.partner'].search(['id','=',self.id]).ids
# #         print self.ids
#  
#     @api.constrains('cust_id')
#     def _check_something(self):
#   
#         if self.cust_id <=0:
#          
#             raise Warning("Your record is too gfgfdgold: %s" )  
class add_deposit_items(models.TransientModel):
    _name = "add.deposit.items"
    _description = "Add Deposit Items"
    
    @api.multi
    def set_button(self):
        res=[]
        res=self.env['add.deposit.items'].search([('id','=',self.id)])
        self.write({'select': True})
        
        
