from openerp import models,fields,api,_ 
from datetime import datetime
import time
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from dateutil.relativedelta import relativedelta
from openerp.tools.translate import _

class admin_school(models.Model):
    _name="student.attendance"
    _rec_name="name"

    name=fields.Many2one('enrolment',)
    std=fields.Char(related='name.standard')
    attendance=fields.Selection([("absent","absent"),('present','present')])
    date=fields.Date(default=datetime.today())
    enrolment_number=fields.Char(related='name.enrolment_number')
    absent=fields.Integer()
    present=fields.Integer()
    working_date=fields.Datetime(default=datetime.today())
    working_days=fields.Integer()
    working_years=fields.Integer()
    n_absent=fields.Integer()
    n_present=fields.Integer()
    fname=fields.Char()
    check=fields.Boolean(string="check attendance")
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'),('cancel', 'Cancel'),('done', 'Done')], required=True, default='draft')
    _sql_constraints=[('record_check','UNIQUE(name,date)','Record already exits')]
   


    
 
    @api.onchange('attendance')
    def onchange_admin(self):
        if self.attendance=='absent':
            self.absent=1
            self.present=0
        
        if self.attendance=='present':
            self.present=1
            self.absent=0  
           
           
           
    @api.one
    @api.onchange('working_date')
    def staff_working(self):
        now=datetime.now()
        dob=datetime.strptime(self.working_date,DEFAULT_SERVER_DATETIME_FORMAT)
        delta=relativedelta(now,dob)
        self.working_years=delta.years
        self.working_days=(now-dob).days
         
           
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
        
        
    @api.multi
    def check_attendance(self):
        res= self.env['enrolment'].search([('id','=',self.name.id)]).name
        r=self.search([('name','=',res)])
        a=0
        b=0
        for x in r:
            
            if(x.attendance=='absent'):
                a=a+1
                self.n_absent= a
            if(x.attendance=='present'):
                b=b+1
                self.n_present= b       
      
        
#         res= self.search_count([('attendance','=','absent'),('id','=',self.name.id)])      
#         self.n_absent=res.attendance
#         self.fname=res.name        

        
#     @api.onchange('attendance')
#     def onchange_date_attendance(self):
#         temp_date=datetime.strptime(self.date_attendance,'%Y-%m-%d %H:%M:%S')
#         self.day_attendance=temp_date.day
#         self.month_attendance=temp_date.month
#         self.year_attendance=temp_date.year
#                    op_list=self.env['student.attendance'].search_count([('attendance','=','absent')])
#         self.n_absent=op_list.absent










#  c=0
#         for x in range(0,len(res),1):
#             c=c+1
#         
#         self.n_absent= c 
#            
#     @api.multi
#     @api.depends('seats','attendees')
#     def calculate_occupation(self):
#         for rec in self:
#             if rec.seats:
#                 rec.occupation =  len(rec.attendees) * 100.0 / rec.seats
#             else:
#                 rec.occupation = 0
           
#          for x in xrange(0<=22):
                
#     @api.depends('total_leave')
#     def onchange_leave(self):
#         if self.leave_days>=1:
#             self.total_leave=self.leave_days+1
# #          
#                
#   
#     @api.multi
#     def check_search(self):
#         if 
#         res= self.search([('age','=','52')])
#         for record in res:
#             record.write({'age': '30'})    


# def my_range(start, end, step):
#     while start <= end:
#         yield start
#         start += step
# 
# for x in my_range(1, 10, 0.5):
#     print x 
#     