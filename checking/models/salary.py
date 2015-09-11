from openerp import models, fields, api, _
import datetime
import time
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from dateutil.relativedelta import relativedelta
import calendar

class salary_amt(models.Model):
    _name="salary.admin"

    salary_date=fields.Datetime(string="Salary date:",default=datetime.datetime.today())
    
    @api.multi
    def provide_salary_func(self):
#         print self.salary_date
        sal_date=datetime.datetime.strptime(self.salary_date,'%Y-%m-%d %H:%M:%S')
        res = self.env['attend.details'].search([])
        c=0
        for rd in res:
            id_sch=self.env['mark.attendance'].search([('emp_name_mark','=',rd.id)])
            
            for ids in id_sch:
#                 print ids.emp_name_mark.empname
                attend_date=datetime.datetime.strptime(ids.date_attendance,'%Y-%m-%d %H:%M:%S')
#                 print ids.emp_name_mark.id
                if(rd.id==ids.emp_name_mark.id and sal_date.year==attend_date.year and sal_date.month==attend_date.month and ids.set_attendance=='ab'):
                    c=c+1
            gp=float(float(rd.basic_pay)-float(float(float(rd.basic_pay)/30)*float(c)))+float(rd.hra_allowance)+float(rd.d_allowance)
            np=gp-float(rd.deduction)
            print np
            print rd.id,rd.basic_pay
            c=0
            
            
#         bp=5000
#         print float(bp/float(calendar.monthrange(2015, 1)[1]))
        
        
#         now = datetime.now()
#         dob = datetime.strptime(self.salary_date, DEFAULT_SERVER_DATETIME_FORMAT)
#         delta = relativedelta(now, dob)