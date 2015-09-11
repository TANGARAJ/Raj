from openerp import models, fields, api, _

class Course(models.Model):
    _name = 'openacademy.course'
    
    name = fields.Char(string='Title', required=True)
    image = fields.Binary()
    description = fields.Text()
    html = fields.Html()
    responsible = fields.Many2one('res.users')
    sessions = fields.One2many('openacademy.session','course', copy=False)

    @api.model
    def create(self, values):
        #add your code here
        return super(Course, self).create(values)

    @api.multi
    def write(self, values):
        #add your code here
        return super(Course, self).write(values)

    @api.one
    def copy(self, default):
        default['name'] = self.name + " (copy)" 
        #add your code here
        return super(Course, self).copy(default)

    @api.multi
    def unlink(self):
        #add your code here
        return super(Course, self).unlink()

