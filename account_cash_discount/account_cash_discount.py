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

class account_cash_discount(osv.osv):
  _name = "account.cash.discount"
  _description = "Cash discount on invoices and sale orders."
  _columns = {
    'name' : fields.char('Bezeichnung', size=30, required="True"),
    'discount_deadline' : fields.integer('Skontofrist', size=2, required=True,
        help='Frist in Tagen, wie lange Skonto abgezogen werden darf,'),
    'discount_rate' : fields.float('Skontosatz', digits=(2,2), required=True,
        help='Höhe des Skontos in Prozent.'),
    'net_payment_target' : fields.integer('Netto-Zahlungsziel', size=2,
        required=True, help='Frist in Tagen, bis wann die Rechnung in Netto ' +
        'beglichen werden kann')
    }

class sale_cash_discount(osv.osv):
  _inherit = "sale.order"
  _description = "Adds field for cash discount on sales order form"
 
  '''
  Method computes values for discount amount and the sum to be paid by a specific date
  '''
  def _cash_discount(self, cr, uid, ids, field_name, arg, context=None):
    # Get discount rate for selected cash discount
    res = {}
    discount_obj = self.pool.get('account.cash.discount')
    cur_obj = self.pool.get('res.currency')
    for order in self.browse(cr, uid, ids, context=None):
      res[order.id] = {
                       'discount_amount' : 0.0,
                       'discount date' : '',
                       'discount_sum' : 0.0,
                       }
      if discount_obj and order.cash_discount.id:
        # Compute discount amount and new price
        discount_rate = discount_obj.browse(cr, uid, order.cash_discount.id).discount_rate
        discount_amount = order.amount_total * discount_rate / 100
        discount_sum = order.amount_total - discount_amount
        
        # Compute deadline for discount payment
        discount_days = discount_obj.browse(cr, uid, order.cash_discount.id).discount_deadline
        date_order = datetime.datetime.strptime(order.date_order, '%Y-%m-%d %H:%M:%S')
        discount_date = date_order + datetime.timedelta(discount_days)
        
        # Prepare data 
        cur = order.pricelist_id.currency_id
        res[order.id]['discount_amount'] = cur_obj.round(cr, uid, cur, discount_amount)
        res[order.id]['discount_sum'] = cur_obj.round(cr, uid, cur, discount_sum)
        res[order.id]['discount_date'] = discount_date.date()
    return res

  _columns = {
      'cash_discount' : fields.many2one('account.cash.discount', 'Skonto'),
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
      'discount_sum' :fields.function(
        _cash_discount,
        digits_compute=dp.get_precision('Account'),
        string='Rechnungsbetrag abzgl. Skonto',
        multi='cash_discount'),
      }
