from openerp import models,fields,api,_ 
from datetime import datetime
class teachers_attendance(models.Model):
    _name='teacher.attendance'
    _rec_name="tname"
   
    tname=fields.Many2one('teacher.detail','name')
    attendance_reg=fields.Selection([("absent","absent"),('present','present'),('half_day','half_day')])
    today_date=fields.Date(default=datetime.today())
    leave_day=fields.Integer()
    present_day=fields.Integer()
    n_present=fields.Char()
    n_absent=fields.Char()
    check=fields.Boolean(string="check attendance")
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'),('cancel', 'Cancel'),('done', 'Done')], required=True, default='draft')
    a=fields.Char()
    b=fields.Char()
    c=fields.Char()
    _sql_constraints=[('record_check','UNIQUE(tname,attendance_reg,today_date,leave_day,present_day)','Record already exits')]
  
    
    

    
 

           
           
    @api.onchange('attendance_reg')
    def onchange_teachers(self):
        if self.attendance_reg=='absent':
            self.leave_day=1
            self.present_day=0
        
        if self.attendance_reg=='present':
            self.present_day=1
            self.leave_day=0    
        if self.attendance_reg=='half_day':
            self.present_day=2
            self.leave_day=0                 
            
#             self.present=self.leave_days 
#             self.total_leave=self.leave_days+1 
       
#         if self.present==self.leave_days:
#            self.leave_days=0
        
#            self.present=self.leave_days 
#            self.total_leave=self.leave_days+1 
   
           
           
           
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
    def check_numberofstudent(self):
        res= self.env['teacher.detail'].search([('id','=',self.tname.id)]).name
        r=self.search([('tname','=',res)])
        a=0
        b=0
        c=0
        for x in r:
            
            if(x.attendance_reg=='absent'):
                a=a+1
                self.n_absent= a
            if(x.attendance_reg=='present'):
                b=b+1
                self.n_present= b      
            if (x.attendance_reg=='half_day'):
                c=c+1
                self.n_present= c
                
    @api.multi       
    def button_select_check(self):
        res= self.env['teacher.detail'].search([('id','=',self.tname.id)]).name
        self.a= self.today_date
        self.b= self.n_present
        self.c= self.attendance_reg
        print self.leave_day
        print res
    @api.multi
    def unlinkkkk(self):
        res= self.env['teacher.detail'].search([('id','=',self.tname.id)]).name
        self.a= " "
        self.b= ""
        self.c= " "
            
        #     @api.one() 
#     def get_services(self, cr, uid, ids, context=None):
#         values = cr.execute("""SELECT name, entity
#                             FROM admin.school WHERE id = 3""")
#         values.fetchall()
#         for value__ in values:
#             if value__:
#                 return {'value': {'service_id': value__[0] + " | " + value__[1]},} # Example: "Service 1 | Google"
    