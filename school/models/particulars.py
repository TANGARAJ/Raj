from openerp import models,fields,api,_ 

class particulars(models.Model):
    _name="particulars.student"
    
#     
#     name=fields.Char()
    enrolment_number=fields.Char(required=True)
    find_rollno=fields.Char()
    find_name=fields.Char()
    m1=fields.Integer()
    m2=fields.Integer()
    m3=fields.Integer()
    m4=fields.Integer()
    m5=fields.Integer()
    total=fields.Char()
    result=fields.Char()
    grade=fields.Char()
    
    
    
    
    @api.multi
    def check_search(self):
    
        res= self.env['subject.details'].search([('enrolment_number','=',self.enrolment_number)])
        self.find_rollno=res.enrolment_number
        self.find_name=res.name.name
        self.m1=res.s1_tamil
        self.m2=res.s2_english
        self.m3=res.s3_maths
        self.m4=res.s4_science
        self.m5=res.s5_social
        self.grade=res.grade
        self.total=res.total
        self.result=res.status

    @api.multi
    def result_search(self):
        res_ids=self.env['subject.details'].search([('id','=',self.id)]).ids
        print self.env['subject.details'].browse(res_ids)
        print self.ids
        
        
        
        
        
        
#     @api.multi
#     def open_popup(self, ids, context=None):
#         if self.name==self.rollno:
#             win_obj = self.pool.get('ir.actions.act_window')
#             res = win_obj.for_xml_id( 'subject_details', 'action_particulars_id', context)
#             return res