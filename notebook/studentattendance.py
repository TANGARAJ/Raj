from openerp.osv import orm, fields

class student_attendance(orm.Model):

    _inherit="hr.attendance"     
    _recname="student_name"
    _columns={
        'student':fields.boolean('student'), 
        'student_name':fields.many2one('res.partner','student_name',domain=[('student','=',True)]),
        'standard':fields.char('standard',related='student_name.standard'),
        }