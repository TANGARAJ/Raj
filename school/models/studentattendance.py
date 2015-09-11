from openerp import models,fields,api,_ 

class student_attendance(models.Model):

    _inherit="hr.attendance"     
    _recname="student_name"
    
    student=fields.Boolean()
    student_name=fields.Many2one('res.partner',domain=[('student','=',True)])
    standard=fields.Char(related='student_name.standard')