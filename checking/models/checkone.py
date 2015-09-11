from openerp import models,fields,api,_ 
from datetime import datetime

class fCheck_account(models.Model):

    _name='check.one'
    _rec_name='accno'
    
    accno=fields.Char()
#     accno=fields.Char(default =lambda self:self.env['ir.sequence'].get('check.one'))
    name=fields.Many2one('res.partner',string='customer',required=True)
    customer_id=fields.One2many('whatever','checkaccno')
    balance=fields.Integer()
    deposite=fields.Integer()
    date=fields.Date(default=datetime.today())
    Acexp=fields.Date()
    address=fields.Char()
    account_type=fields.Selection([('join','join'),('personal','personal'),('group','group')])
#     Grantee = fields.One2many('inher', 'name', string="Process")
    withdraw=fields.Integer()
    actual=fields.Float(compute='check_am', string='current amount',store=True, readonly=False)
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'),('cancel', 'Cancel'),('done', 'Done')], required=True, default='draft')
#     actual=fields.Float()
    image142 = fields.Binary()
    file123 = fields.Binary()
    active =  fields.Boolean(default=True)
    
    
#     _defaults = {'accno': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'telephone'), }
   
    @api.model
    def create(self,vals):
        if not vals:
            vals = {}
        vals['accno'] = self.env['ir.sequence'].get('check.one')
        return super(fCheck_account,self).create(vals)
    
    
    @api.depends('withdraw','deposite','balance') 
    def check_am(self):
        self.actual=self.deposite
        self.actual=self.deposite-self.withdraw
        self.actual=self.balance
        self.balance=self.balance-self.withdraw
       
            
            
#             
#     @api.onchange('withdraw','deposite','balance')
#     def on_chane_actual(self):
# #         self.actual=self.deposite
#         self.actual=self.deposite-self.withdraw
# 
#         self.balance=self.balance-self.withdraw
#         self.actual=self.balance  
#               
    @api.onchange('accno')
    def onchange_accno(self):
        if self.accno:
            self.deposite=10000
        

    @api.onchange('account_type')
    def onchange_account_type(self):
        if self.account_type == 'personal':
              
            self.deposite = 50000
        if self.account_type == 'join':
              
            self.deposite = 25000
        if self.account_type == 'group':
              
            self.deposite = 30000  
    @api.one
    def do_confirm(self):
        self.state = 'confirm'

    @api.one
    def do_done(self):
        self.state = 'done'

    @api.one
    def do_cancel(self):
        self.state = 'cancel'

    @api.one
    def do_reset(self):
        self.state = 'draft'
           
#     def deposite (self, name, balance=0.0):
#         
#         self.name = name
#         self.balance = balance
# 
#     def withdraw(self, actual):
#   
#         if actual > self.balance:
#             raise RuntimeError('Amount greater than available balance.')
#         self.balance -= actual
#         return self.balance
# 
#     def deposit(self, actual):
#   
#         self.balance += actual
#         return self.balance          
#            
    



           
#             self.accno=self.accno+ 'deposite '
#         if self.accno and not self.name:
           
#             self.deposite=0
#             if self.accno and not self.name:
#                 self.name = self.accno.name + 'deposite '
#                 self.deposite=1000
#             if self.accno.name == '':
# #                 self.Acexp=Date()
#                 self.date=datetime.today()
#                 self.deposite = 100000
#                 self.duration=100.0        
        
# def bar(actual, withdraw, balance, **options):
#     if options.get("action") == "sum":
#         print "The sum is: %d" % (actual + withdraw - balance)
#  
#     if options.get("number") == "actual":
#         return actual
#  
# result = bar(1, 5, 3, action = "sum", number = "actual")
# print "Result: %d" % result

   
      
#     @api.depends('withdraw','actual') 
#     def check_bal(self):
#     if self.actual=self.deposite):
#             print 'balance'
#             else
#                print 'withdraw'
# #         self.actual=self.deposite-self.withdraw
# 
#    
#    
   
# @api.multi
#     def check_search(self):
#         res= self.search([('age','=','34')])
#         for record in res:
#             record.write({'age': '30'})

class web_example(models.Model):
    _name='test'
    
    numero=fields.Char()
#             