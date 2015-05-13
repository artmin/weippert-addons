# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 artmin - IT Dienstleistungen.
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

class stock_picking(osv.osv):
    _inherit = 'stock.picking'

    # Get the first product of the delivery order so it can be displayed in the
    # list view
    def _first_product(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        # Get first product of each delivery order
        for delivery_order in self.browse(cr, uid, ids, context=None):
          if delivery_order.move_lines and len(delivery_order.move_lines) > 0:
            res[delivery_order.id] = delivery_order.move_lines[0].name
          else:
            res[delivery_order.id] = ''
        return res
 
    _columns = {
        'first_product' : fields.function(
          _first_product,
          type='char',
          string="Artikel"),
        'client_order_ref' : fields.related(
            'sale_id',
            'client_order_ref',
            type="char",
            relation="sale.order",
            string="Bestellnummer",
            store=False),
        'custom_delivery_date' : fields.related(
            'sale_id',
            'custom_delivery_date',
            type="date",
            relation="sale.order",
            string="Wunschtermin Lieferung",
            store=False),
        }
