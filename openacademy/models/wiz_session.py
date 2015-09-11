from openerp import models, fields, api

class Session(models.TransientModel):

    _name = 'wiz.openacademy.session'

    sessions = fields.One2many('wiz.openacademy.session.data','wiz_id')
    different_data = fields.Boolean()
    
    @api.one
    def add_session(self):
        session_obj = self.env['openacademy.session']
        for session in self.sessions:
            old_session = session_obj.search([("course",'=',session.course.id),("start_date","=",session.date)])
            if old_session:
                old_session.write({"name":session.name,"description": session.description})
            else:
                value = {"name":session.name,
                     "course":session.course.id,
                     "description": session.description,
                     "start_date": session.date
                     }
                session_obj.create(value)

class SessionData(models.TransientModel):

    _name = 'wiz.openacademy.session.data'

    wiz_id = fields.Many2one('wiz.openacademy.session')
    name =  fields.Char()
    course =  fields.Many2one('openacademy.course')
    description = fields.Text()
    date = fields.Date() 

