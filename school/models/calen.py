from datetime import timedelta
from openerp import models, fields, api, exceptions

class Course_check(models.Model):
    _name="course.check"

    attendee_ids = fields.Many2one('res.partner')
    name=fields.Char()
    taken_seats = fields.Float(string="Taken seats")
    start_date=fields.Date(string='start_date')
    end_date = fields.Date(string="End Date", store=True)
    instructor_id=fields.Char()
    country_id=fields.Char()
    
    
    
    @api.onchange('attendee_ids')
    def onchange_run(self):
        student_obj=self.env['res.partner'].search([('id','=',self.attendee_ids.id)])
        self.country_id=student_obj.country_id.name
        self.instructor_id=student_obj.application_number
        self.start_date=student_obj.dob
#     compute='_get_end_date', inverse='_set_end_date')
# # 
# #     @api.one
# #     @api.depends('seats', 'attendee_ids')
# # 
# #             }
# 
#     @api.one
#     @api.depends('start_date', 'duration')
#     def _get_end_date(self):
#         if not (self.start_date and self.duration):
#             self.end_date = self.start_date
#             return
# 
#         # Add duration to start_date, but: Monday + 5 days = Saturday, so
#         # subtract one second to get on Friday instead
#         start = fields.Datetime.from_string(self.start_date)
#         duration = timedelta(days=self.duration, seconds=-1)
#         self.end_date = start + duration
# 
#     @api.one
#     def _set_end_date(self):
#         if not (self.start_date and self.end_date):
#             return
# 
#         # Compute the difference between dates, but: Friday - Monday = 4 days,
#         # so add one day to get 5 days instead
#         start_date = fields.Datetime.from_string(self.start_date)
#         end_date = fields.Datetime.from_string(self.end_date)
#         self.duration = (end_date - start_date).days + 1
# 
# #     @api.one
# #     @api.constrains('instructor_id', 'attendee_ids')
# #     def _check_instructor_not_in_attendees(self):
# #         if self.instructor_id and self.instructor_id in self.attendee_ids:

