from openerp import models,fields,api,_ 
from datetime import datetime
import random
class timetable(models.Model):
    _name="time.table"
    _rec_name="timetable"

    timetable=fields.Selection([('VI','VI'),('VII','VII'),('VIII','VIII'),('IX','IX'),('X','X')])
    days=fields.Selection([('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday')])
    date=fields.Date(default=datetime.today())
   
#     mon=fields.Char(readonly=True)
#     tue=fields.Char(readonly=True)
#     wed=fields.Char(readonly=True)
#     thu=fields.Char(readonly=True)
#     fri=fields.Char(readonly=True)
#     
    hr1=fields.Char()
    hr2=fields.Char()
    hr3=fields.Char()
    hr4=fields.Char()
    hr5=fields.Char()
    
   

   
   
#     @api.multi
#     def check_search(self):
#       
#         res= ['time.table'].search([('timetable','=',self.timetable),])
#         self.find_rollno=res.enrolment_number
#         self.find_name=res.student_name.name
        
    
    @api.onchange('days','timetable')
    def onchange_mon(self):   
        mon = ['tamil','english','science','social','maths']
        random.shuffle(mon,random.random)
        list=[]
        list=mon
        self.hr1=list[0]
        self.hr2=list[1]
        self.hr3=list[2]
        self.hr4=list[3]
        self.hr5=list[4]
        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        

# 
#     @api.multi
#     def time_table(self):
#             
#         record_ids = [{'hr1':'tamil'},
#                      {'hr2':'english'},
#                       {'hr3':'maths'},{'hr4':'science'},{'hr5':'social'}]
#         for mon in record_ids:
#             for item in mon.iteritems():
#                 print item[0],item[1]
    
#     days=fields.Selection([('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday')])
#     standard=fields.Selection([('VI','VI'),('VII','VII'),('VIII','VIII'),('IX','IX'),('X','X')])
#     I_hour=fields.Selection([('T','T'),('M','M'),('E','E'),('S','S'),('SO','SO')])
#     II_hour=fields.Selection([('E','E'),('M','M'),('S','S'),('SO','SO'),('PT','PT')])
#     III_hour=fields.Selection([('M','M'),('E','E'),('SO','SO'),('S','S'),('GK','GK')])
#     IV_hour=fields.Selection([('S','S'),('T','T'),('SO','SO'),('E','E'),('DW','DW')])
#     V_hour=fields.Selection([('T','T'),('S','S'),('E','E'),('M','M'),('PT','PT')])