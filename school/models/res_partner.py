from openerp import models,fields,api,_

class Partner(models.Model):
    _inherit = 'res.partner'
    
    student = fields.Boolean()
    application_number=fields.Char(required=True, default =lambda self:self.env['ir.sequence'].get('res.partner'))
    standard=fields.Char(required=True)   
    enrolment_number=fields.Char()
    dob=fields.Date()