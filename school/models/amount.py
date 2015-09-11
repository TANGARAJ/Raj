from openerp.osv import fields, osv
from openerp import models,fields,api,_ 
# from tools.translate import _
from openerp.tools import amount_to_text_en
from openerp.tools.amount_to_text_en import amount_to_text 
from openerp.osv import orm, fields


class sale_order(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Order"
    
    amount_words=fields.Integer(compute='_amount_in_words', string='In Words',  store=True)
    
    @api.depends()
    def _amount_in_words(self,field_name,order):
        cur_obj = self.env['res.currency']
        res = {}
#         for order in self.browse(cr, uid, ids, context=context):
        taxed = untaxed = 0.0
        res[order.id] = {
            'amount_words': '0.0',
                        }
        val = val1 = 0.0
        cur = order.pricelist_id.currency_id
        for line in order.order_line:
            val1 += line.price_subtotal
            val += self._amount_line_tax(line)
        taxed = cur_obj.round(val)
        untaxed = cur_obj.round(val1)
        res[order.id] = amount_to_text_en.amount_to_text(float(taxed + untaxed))
        return res


       



sale_order()