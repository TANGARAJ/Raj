from openerp import models, fields, api
from openerp.exceptions import Warning
from datetime import datetime, timedelta

class Session(models.Model):

    _name = 'openacademy.session'
    
    name = fields.Char(required=True)
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'),('cancel', 'Cancel'),('done', 'Done')], required=True, default='draft')
    duration = fields.Float()
    seats = fields.Integer()
    start_date =  fields.Date()
    end_date =  fields.Date()
    active =  fields.Boolean(default=True)
    description =  fields.Text()
    course = fields.Many2one('openacademy.course')
    instructor = fields.Many2one('res.partner')
    attendees = fields.Many2many('res.partner')
    occupation = fields.Float(compute="calculate_occupation")
    course_info = fields.Text(related="course.description")
    upper = fields.Char(compute='_compute_upper',
                        inverse='_inverse_upper')
     
    @api.depends('name')
    def _compute_upper(self):
        for rec in self:
            rec.upper = rec.name.upper() if rec.name else False
 
    def _inverse_upper(self):
        for rec in self:
            rec.name = rec.upper.lower() if rec.upper else False
            
    @api.onchange('course')
    def onchange_course(self):
        if self.course:
            self.seats=0
            if self.course and not self.name:
                self.name = self.course.name + ' Session'
            if self.course.name == 'english':
                self.start_date=''
                self.end_date=datetime.today()
                self.seats = 10
                self.duration=100.0
                
    @api.onchange('instructor')
    def onchange_instructor(self):
        if self.instructor == 'Agrolait':
            self.duration=50.0
            self.start_date=datetime.today()
            self.description="test"
            if self.duration > 20:
                raise Warning('Warning')

    @api.constrains('attendee','instructor')
    def attendee_constrains(self):
        if self.instructor.id in self.attendees.ids:
            raise Warning('You can not add instructor as a attendee')
    
    @api.multi
    @api.depends('seats','attendees')
    def calculate_occupation(self):
        for rec in self:
            if rec.seats:
                rec.occupation =  len(rec.attendees) * 100.0 / rec.seats
            else:
                rec.occupation = 0
    
    @api.one
    def do_confirm(self):
        self.state = 'confirm'

    @api.one
    def do_done(self):
        self.state = 'done'

    @api.one
    def do_cancel(self):
        self.state = 'cancel'

    @api.one
    def do_reset(self):
        self.state = 'draft'

