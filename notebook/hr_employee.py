from openerp.osv import orm, fields
from datetime import datetime

class employee_staff(orm.Model):
    _inherit='hr.employee'
    _columns={
    'staff':fields.boolean('staff'),
    'qualification':fields.char('qualification'),
    'handling_subject':fields.char('handling_subject'),
    'standards':fields.char('standards')
    }
#     timetable=fields.Selection([('VI','VI'),('VII','VII'),('VIII','VIII'),('IX','IX'),('X','X')])
#     present_day=fields.Date()
#     days=fields.Selection([('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday')])
#     hr1=fields.Char()
#     hr2=fields.Char()
#     hr3=fields.Char()
#     hr4=fields.Char()
#     hr5=fields.Char()
#      
#     _sql_constraints = [      
# 
#         ('staff_id_unique',
#          'UNIQUE(staff_id)',
#          "The staff id is already exist "),
#     ]
#     
#     @api.multi
#     def check_timetable(self):
#     
#         res= self.env['time.table'].search([('days','=',self.days),('timetable','=',self.timetable)])
#         
#         self.hr1=res.hr1
#         self.hr2=res.hr2
#         self.hr3=res.hr3
#         self.hr4=res.hr4
#         self.hr5=res.hr5
#         
#     @api.model
#     def _needaction_count(self, domain=None):
#         res=self.search([])
#         c=0
#         for x in range(0,len(res),1):
#             c=c+1
#          
#         return c 