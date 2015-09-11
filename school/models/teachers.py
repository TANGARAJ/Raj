from openerp import models,fields,api,_ 
from openerp.exceptions import Warning, ValidationError
from datetime import datetime
import time

class teachers(models.Model):
    _name="teacher.detail"
    _inherit = ['ir.needaction_mixin']
    _rec_name='name'
    
    name=fields.Char(required=True)
    surname=fields.One2many('student.regis','name',order="name.sort()")
    designation=fields.Char()
    qualification=fields.Char()
    staff_id=fields.Char()
    handling_subjects=fields.Selection([('tamil','tamil'),('english','english'),('maths','maths'),('science','science'),('social','social')])
    timetable=fields.Selection([('VI','VI'),('VII','VII'),('VIII','VIII'),('IX','IX'),('X','X')])
    select=fields.Boolean()
#     current_time=fields.Char(string="Current Time: ",default=time.strftime('%I:%M:%S'),readonly=True) 
#     days=fields.Selection([('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday')])
    feedback=fields.Text()
    present_day=fields.Date()
    days=fields.Selection([('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday')])
    hr1=fields.Char()
    hr2=fields.Char()
    hr3=fields.Char()
    hr4=fields.Char()
    hr5=fields.Char()
     
    _sql_constraints = [      

        ('staff_id_unique',
         'UNIQUE(staff_id)',
         "The staff id is already exist "),
    ]

    @api.multi
    def check_timetable(self):
    
        res= self.env['time.table'].search([('days','=',self.days),('timetable','=',self.timetable)])
        
        self.hr1=res.hr1
        self.hr2=res.hr2
        self.hr3=res.hr3
        self.hr4=res.hr4
        self.hr5=res.hr5
        
        
        
    @api.model
    def _needaction_domain_get(self):
        return [('state', '=', 'new')]    
        
    @api.model
    def _needaction_count(self, domain=None):
        res=self.search([])
        c=0
        for x in range(0,len(res),1):
            c=c+1
        self.write({'select': 'True'})
        return c    
         
#     
#     @api.one
#     @api.constrains('staff_id')
#     def _check_const(self):
#         if  (self.staff_id==self.staff_id):
#             raise ValidationError("staff id is already used") 


