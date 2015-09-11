from openerp.osv import orm, fields
from datetime import datetime

class student_customer(orm.Model):
    _inherit = 'res.partner'
    _columns={
        'student':fields.boolean('student'),
        'application_number':fields.char('application_number'),
    
        'standard':fields.char('standard',required=True),   
        'enrolment_number':fields.char('enrolment_number'),
        'dob':fields.date('dob'),
        }
    _defaults = {'application_number': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'res.partner'),}