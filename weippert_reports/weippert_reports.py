# -*- coding: utf-8 -*-
##############################################################################
#
#    it.artmin - Martin Apitz
#    Copyright (C) 2014 (<http://it.artmin.de>).
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

class weippert_sale_order(osv.osv):
  _inherit = 'sale.order'

  # Modify method that is invoked by print button
  def print_quotation(self, cr, uid, ids, context=None):
    '''
    This function prints the sales order and mark it as sent, so that we can
    see more easily the next step of the workflow
    '''

    assert len(ids) == 1, 'This option should only be used for a single id at a time'
    self.signal_quotation_sent(cr, uid, ids)
    return self.pool['report'].get_action(
      cr, uid, ids, 'sale.report_saleorder.webkit', context=context)

weippert_sale_order()
