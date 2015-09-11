from openerp import models,api,fields,_ 

class wiz_form(models.TransientModel):
    _name = 'wiz'
   
   
   
    tname=fields.Char('Name 1')
    pname= fields.Char('Name 2')
    state = fields.Selection([('step1', 'step1'),('step2', 'step2')])  
               
    @api.multi
    def action_next(self):
        self.write({'state': 'step1'})
        print 'tangaraj'
        
        
        
    @api.multi
    def action_previous(self):
        #your treatment to click  button previous 
        #...
        # update state to  step1
        self.write( {'state': 'step1',})
        #return view
#         return {
#             'type': 'ir.actions.act_window',
#                 'res_model': 'newmodule',
#                 'view_mode': 'form',
#                 'res_id': ' ',
#                 'view_type': 'form',
#                 'target': 'new',
#                  }
 