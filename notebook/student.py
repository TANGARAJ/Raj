from openerp.osv import orm, fields
from datetime import datetime
class student(orm.Model):
    _name = 'student'
    _columns = {
        'name':fields.char('name',required=True),
        'surname':fields.char('surname'),
        'age':fields.integer('age',required=True),
        'Division':fields.char('Division'), 
        'standard':fields.char('standard',required=True),   
        'address':fields.text('address',reqiured=True),
        'dob':fields.date('dob',reqiured=True),
        'enrolment_number':fields.char('enrolment_number'),
        'gender':fields.selection((('male','male'),('female','female')),'gender'),
        'state_id':fields.many2one('res.country.state','state_id'),
        'country_id':fields.many2one('res.country','country_id'),
        'adm_date':fields.date('adm_date'),
        'nationality':fields.selection((('indian','indian'),('others','others')),'nationality'),
        'contact_number':fields.integer('contact_number',reqiured=True),
    }
    
    
#     def onchange_getage_id(self,cr,uid,ids,dob,context=None):
#     current_date=datetime.now()
#     current_year=current_date.year
#     birth_date = parser.parse(dob)
#     current_age=current_year-birth_date.year
#      val = {
#         'age_text':current_age
#     }
#     return {'value': val}

    
#       def on_change_dob(self, cr, uid, ids, date_of_birth, context=None ):
#        re={}
#        if date_of_birth :
#            current_age = datetime.now().year - parser.parse(date_of_birth).year
#            re['age']=current_age
#        return {'value':re}