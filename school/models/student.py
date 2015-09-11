from openerp import models,fields,api,_ 
from datetime import datetime
import re

class school_student(models.Model):
    
    _name="student.regis"
    _inherits={'enrolment':'id1'}
    _inherit = ['ir.needaction_mixin']
    
    id1=fields.Many2one('enrolment',required=True,ondelete='cascade')
    serial_number=fields.Char(required=True, default =lambda self:self.env['ir.sequence'].get('student.regis'))
    image142 = fields.Binary()
    
    _defaults = {'serial_number': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'student.regis'), }
    
         
    @api.onchange('state_id')
    def onchange_state(self):
        if self.state_id:
            self.country_id=self.state_id.country_id.id
            
       
            
            
            
    @api.model
    def _needaction_count(self, domain=None):
        res=self.search([])
        c=0
        for x in range(0,len(res),1):
            c=c+1
         
        return c    
    @api.model
    def _context_check(self):
        for student_id in self:
            if student_id.student_regis:
                self.student_id.with_context(tan=True)._needaction_count()
#                 ctx=dict(self._context)
                
#     name=fields.Char(required=True)
#     regno=fields.Char(required=True)

#     age=fields.Integer(required=True)
#     address=fields.Char()
#     gender=fields.Selection([('male','male'),('female','female')])
#     state=fields.Many2one('res.country.state')
#     country=fields.Many2one('res.country')
#     reg_date=fields.Date(default=datetime.today())
#     contact=fields.Char()   
   
    

#     @api.one
#     @api.depends('name', 'parent.display_name')     # this definition is recursive
#     def _compute_display_name(self):
#         if self.parent:
#             self.display_name = self.parent.display_name + ' / ' + self.name
#         else:
#             self.display_name = self.name
class child1(models.Model):
    _name="enrolment"
    _rec_name="name"
     
    name=fields.Char(required=True)
    surname=fields.Char()
    age=fields.Integer(required=True)
    Division=fields.Char() 
    standard=fields.Char(required=True)   
    address=fields.Text(reqiured=True)
    dob=fields.Date(reqiured=True)
    enrolment_number=fields.Char()
    gender=fields.Selection([('male','male'),('female','female')])
    state_id=fields.Many2one('res.country.state')
    country_id=fields.Many2one('res.country')
    adm_date=fields.Date()
    nationality=fields.Selection([('indian','indian'),('others','others')])
    contact_number=fields.Integer(reqiured=True)
    share=fields.Selection([('like','LIke'),('Sign','sign')])
     
    @api.onchange('state_id')
    def onchange_state(self):
        if self.state_id:
            self.country_id=self.state_id.country_id.id
            
            
    @api.onchange('share','age')
    def onchange_share(self):
        if self.age==20:
            self.share='like'
        else:
            self.share="Sign"    