from openerp import models, fields, api, _

class testing(models.Model):
    _name='testing'
    
    many_ids=fields.Many2many('newmodule','testing_table','name')
    testing=fields.Char()
    
    
    
class testing_two(models.Model):
    _name='testing.two'
    
    checking=fields.Many2one('newmodule','name')    
    
    
class account_bank_statement(models.Model):
    _inherit="account.bank.statement"

    @api.onchange
    def onchange_journal_id(self, statement_id, journal_id):
        if not journal_id:
            return {}
        balance_start = self._compute_balance_end_real(journal_id)
#             journal = self.pool.get('account.journal').browse(journal_id)
        journal = self.env['account.journal'].search([('journal_id','=', self.id)])
        currency = journal.currency or journal.company_id.currency_id
        res = {'balance_start': balance_start, 'company_id': journal.company_id.id, 'currency': currency.id}
        if journal.type == 'cash':
            res['cash_control'] = journal.cash_control
        return {'value': res}    