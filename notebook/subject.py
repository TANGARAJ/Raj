from openerp.osv import orm, fields
from datetime import datetime


from openerp.exceptions import Warning, ValidationError

class subjects(orm.Model):
    _name="subject.details"
    
#     def fnct(self, cr, uid, ids, field_name, arg, context):
#         res = {}
#         self_id = self.browse(self, cr, uid, ids, context=context)
#         res[self_id.id] = 'test'
#         return res
#     
#     def multi_price_qty(self, cr, uid, ids, name, arg, context=None):
#         res = {}
#         for product in self.browse(cr, uid, ids,context):
#             res[product.id] = product.price * product.qty
#         return res
    
    _columns={
            'tname':fields.many2one('hr.employee','tname',domain=[('staff','=',True)]),
            'name':fields.many2one('res.partner','name',required=True,domain=[('student','=',True)]),
            'enrolment_number':fields.related('name','enrolment_number',type='many2one',relation='res.partner', string='standard'),
            'std':fields.related('std','name.standard'),
            's1_tamil':fields.integer('s1_tamil'),
            's2_english':fields.integer('s2_english'),
            's3_maths':fields.integer('s3_maths'),
            's4_science':fields.integer('s4_science'),
            's5_social':fields.integer('s5_social'),
            'total':fields.float('total'),
            'grade':fields.char('grade'),
            'avg':fields.float('avg'),
            'status':fields.char('status'),
#             'test_function': fields.function(fnct, string="Test Function"),
#             'totalprice': fields.function(multi_price_qty, type='integer', 'Total Price'),
    }
    
   

    
    def onchange_total(self, cr, uid, ids, s1_tamil, s2_english,s3_maths,s4_science,s5_social,total):
#         return {'sum':num1+num2}
        return {'value': {'total':s1_tamil+s2_english+s3_maths+s4_science+s5_social,'avg':total/5}}
        
        
     
#     def on_change_average_id(self, cr, uid, ids,total):
#         return{'value':{'avg':total/5}}
        
#         
# 
# 
    def rang_func(self, cr, uid, ids,grade,avg):
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
# 
#      
#  
#     def onchange_sums(self, cr, uid, ids,s1_tamil,s2_english,s3_maths,s4_science,s5_social):
#         status='fail'    
#         if s1_tamil>=35 and s2_english>=35 and s3_maths>=35 and s4_science>=35 and s5_social>=35:
#                    self. status='pass'   
# #                
#             
# 
#     @api.one
#     @api.constrains('s1_tamil','s2_english','s3_maths','s4_science','s5_social')
#     def _check_const(self):
#         if  (self.s1_tamil>100) or (self.s2_english>100) or (self.s3_maths>100) or (self.s4_science>100) or (self.s5_social>100):
#             raise ValidationError("mark is not allowed") 
        
        
# def _score_calc(self,cr,uid,ids,field,arg,context=None):
# 
#     res = {}
#     
#     # This loop generates only 2 queries thanks to browse()!
#     
#     for idea in self.browse(cr,uid,ids,context=context):
#     
#         sum_vote = sum([v.vote for v in idea.vote_ids])
#         avg_vote = sum_vote/len(idea.vote_ids)
#         res[idea.id] = avg_vote
#     return res
# _columns = {
# # Replace static score with average of votes
# 'score':fields.function(_score_calc,type='float')
# }
#         
#      
#     def name_get(self,cr,uid,ids):
#         res = []
#         for r in self.read(cr,uid,ids['name','create_date'])
#           res.append((r['id'], '%s (%s)' (r['name'],year))
#         return res   
#           
      
      