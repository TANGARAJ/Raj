from openerp import models,fields,api,_ 
from openerp.exceptions import Warning, ValidationError

class subjects(models.Model):
    _name="subject.details"
    _rec_name="name"

    tname=fields.Many2one('hr.employee','name')
    name=fields.Many2one('res.partner',required=True,domain=[('student','=',True)])
    enrolment_number=fields.Char(related='name.enrolment_number')
    std=fields.Char(related='name.standard')
    s1_tamil=fields.Integer()
    s2_english=fields.Integer()
    s3_maths=fields.Integer()
    s4_science=fields.Integer()
    s5_social=fields.Integer()
    total=fields.Float(compute='comp_function', readonly=False, store=True)
    grade=fields.Char(compute='comp_function', readonly=True, store=True)
    avg=fields.Float(compute='compute_func', readonly=True)
    status=fields.Char()
    #     tname=fields.Many2one('teacher.detail',domain=[('staff','=',True)])
    
    @api.depends('s1_tamil','s2_english','s3_maths','s4_science','s5_social','total','avg') 
    def comp_function(self):
        self.total=self.s1_tamil+self.s2_english+self.s3_maths+self.s4_science+self.s5_social   
        self.avg=self.total/5
        if self.avg>=91:
            self.grade='S'
        elif self.avg>=81 and self.avg<=90:
            self.grade='A'
        elif self.avg>=71 and self.avg<=80:
            self.grade='B'
        elif self.avg>=61 and self.avg<=70:
            self.grade='C'
        elif self.avg>=57 and self.avg<=60:
            self.grade='D'
        elif self.avg>=50 and self.avg<=56:
            self.grade='E'
        else:
            self.grade='U'

    @api.depends('avg')
    def compute_func(self):
        self.avg=self.total/5
        
#     @api.depends()
#     def average_id(self):      

#     @api.depends()
#     def rang_func(self):
#         if self.avg>=91:
#             self.grade='S'
#         elif self.avg>=81 and self.avg<=90:
#             self.grade='A'
#         elif self.avg>=71 and self.avg<=80:
#             self.grade='B'
#         elif self.avg>=61 and self.avg<=70:
#             self.grade='C'
#         elif self.avg>=57 and self.avg<=60:
#             self.grade='D'
#         elif self.avg>=50 and self.avg<=56:
#             self.grade='E'
#         else:
#             self.grade='U'    

     
    @api.onchange('s1_tamil','s2_english','s3_maths','s4_science','s5_social')
    def onchange_result(self):
        self.status='fail'    
        if self.s1_tamil>=35 and self.s2_english>=35 and self.s3_maths>=35 and self.s4_science>=35 and self.s5_social>=35:
            self.status='pass'   
                   

    @api.one
    @api.constrains('s1_tamil','s2_english','s3_maths','s4_science','s5_social')
    def _check_const(self):
        if  (self.s1_tamil>100) or (self.s2_english>100) or (self.s3_maths>100) or (self.s4_science>100) or (self.s5_social>100):
            raise ValidationError("mark is not allowed") 
        
#     @api.model
#     def name_search(self,name='tname', args=None, operator='ilike',limit=100):
#         ids = self.search( [('number', '=', name)] + args, limit=limit)
#         if ids:
#             return self.name_get(self.ids)
