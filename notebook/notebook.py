from openerp.osv import orm, fields

class notebook(orm.Model):
    _name = 'notebook'
    _columns = {
        'name': fields.char('Name', size=40),
        'text': fields.text('text'),
        'num1': fields.float('num1'),
        'num2': fields.float('num2'),
        'sum': fields.float('sum'),
    }
    
    
    
    def onchange_sum(self, cr, uid, ids, num1, num2):
#         return {'sum':num1+num2}
        return {'value': {'sum':num1+num2}}
            