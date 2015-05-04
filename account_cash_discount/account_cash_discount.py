# -*- coding: utf-8 -*-
##############################################################################
#
#    it.artmin
#    Martin Apitz, May 2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields
from openerp.addons import decimal_precision as dp
import datetime

# Extend payment term by cash discount
class account_cash_discount(osv.osv):
  _inherit = "account.payment.term"
  _description = "Add cash discount to payment terms."
  _columns = {
    'discount_deadline' : fields.integer('Skontofrist', size=2, required=True,
        help='Frist in Tagen, wie lange Skonto abgezogen werden darf,'),
    'discount_rate' : fields.float('Skontosatz', digits=(2,2), required=True,
        help='Höhe des Skontos in Prozent.'),
    'net_payment_target' : fields.integer('Netto-Zahlungsziel', size=2,
        required=True, help='Frist in Tagen, bis wann die Rechnung in Netto ' +
        'beglichen werden kann')
    }

class invoice_cash_discount(osv.osv):
  _inherit = "account.invoice"
  _description = "Adds field for cash discount on invoice form"
 
  '''
  Method computes values for discount amount and the sum to be paid by a specific date
  '''
  def _cash_discount(self, cr, uid, ids, field_name, arg, context=None):
    # Get discount rate for selected cash discount
    res = {}
    payment_objs = self.pool.get('account.payment.term')
    cur_obj = self.pool.get('res.currency')
    for invoice in self.browse(cr, uid, ids, context=None):
      res[invoice.id] = {
                       'discount_amount' : 0.0,
                       'discount_date' : '',
                       'net_date' : '',
                       'discount_sum' : 0.0,
                       }
      if payment_objs and invoice.payment_term.id:
        # Compute discount amount and new price
        payment_obj = payment_objs.browse(cr, uid, invoice.payment_term.id)
        discount_rate = payment_obj.discount_rate
        discount_amount = invoice.amount_total * discount_rate / 100
        discount_sum = invoice.amount_total - discount_amount
        # Prepare data 
        cur = invoice.currency_id
        res[invoice.id]['discount_amount'] = cur_obj.round(cr, uid, cur, discount_amount)
        res[invoice.id]['discount_sum'] = cur_obj.round(cr, uid, cur, discount_sum)
        
        # Compute deadline for discount and net payment
        if invoice.date_invoice:
          discount_days = payment_obj.discount_deadline
          net_days = payment_obj.net_payment_target
          date_order = datetime.datetime.strptime(invoice.date_invoice, '%Y-%m-%d')
          discount_date = date_order + datetime.timedelta(discount_days)
          net_date = date_order + datetime.timedelta(net_days)
          res[invoice.id]['discount_date'] = discount_date.date()
          res[invoice.id]['net_date'] = net_date.date()

    return res

  _columns = {
      'discount_amount' : fields.function(
        _cash_discount,
        digits_compute=dp.get_precision('Account'),
        string='Skontoabzug',
        multi='cash_discount'),
      'discount_date' : fields.function(
        _cash_discount,
        string='Skontofrist',
        type="date",
        multi='cash_discount'),
      'net_date' : fields.function(
        _cash_discount,
        type="date",
        multi='cash_discount'),
      'discount_sum' : fields.function(
        _cash_discount,
        digits_compute=dp.get_precision('Account'),
        string='Rechnungsbetrag abzgl. Skonto',
        multi='cash_discount'),
      }

'''class account_cash_discount_voucher(model.Model):
  Adds possibility to book cash discount on voucher 
  _columns = {
        'payment_option':fields.selection([
                                           ('without_writeoff', 'Keep Open'),
                                           ('with_writeoff', 'Reconcile Payment Balance'),
                                           ('cash_discount', 'Skonto buchen'),
                                           ], 'Payment Difference', required=True, readonly=True, states={'draft': [('readonly', False)]}, help="This field helps you to choose what you want to do with the eventual difference between the paid amount and the sum of allocated amounts. You can either choose to keep open this difference on the partner's account, or reconcile it with the payment(s)"),
      }
      '''
