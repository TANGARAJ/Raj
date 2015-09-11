from openerp import models,fields,api,_ 
AVAILABLE_PRIORITIES = [('0', 'Very Low'),('1', 'Low'),('2', 'Normal'),('3', 'High'),('4', 'Very High')]

class  student_class(models.Model):
    _name="class.student"
    _rec_name="section"
   
 
        
    
    section=fields.Char()
    division=fields.Char(related='standard.standard')
    standard=fields.Many2many('res.partner','standard')
    no_of_student=fields.Integer()
    student=fields.Integer(string="9th standard")
    set_priority=fields.Selection(AVAILABLE_PRIORITIES, select=True)
    
    
    @api.multi
    def check_attendance(self):
        import smtplib
        
        sender = 'tangam.king@gmail.com'
        receivers = 'tangam.king@gmail.com'
        
        message = """hai da
        """
        
        
        smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(user="tangam.king@gmail.com", password="")
        smtpObj.sendmail(sender, receivers, message)         
        print "Successfully sent email"
#            except SMTPException:
#            print "Error: unable to send email"
#            
# class checking_attendance(models.Model):
#        _name='checking'
#        _inherit = "hr.employee"         
#            
           