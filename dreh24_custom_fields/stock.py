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
        }
       
    # Get custom delivery date from sales order
    def _picking_assign(self, cr, uid, move_ids, procurement_group, location_from, location_to, context=None):

        # Call super function
        res = super(stock_move, self)._picking_assign(cr, uid, move_ids, procurement_group, location_from, location_to, context=context)

        # Get move id
        move = self.browse(cr, uid, move_ids, context=context)[0]

        # Get the values from the move
        order_obj = self.pool.get("sale.order")
        order_id = order_obj.search(cr, uid, [('name','=', move.origin)], context=context)
        vals = order_obj.read(cr, uid, order_id, ['custom_delivery_date'])

        # Get delivery date
        for value in vals:
            if value.has_key('custom_delivery_date'):
                order_ref = value['custom_delivery_date']
        # If exists client reference update stock picking client_order_ref field
        if (len(vals) > 0) and order_ref:
            stock_pick_obj = self.pool.get("stock.picking")
            stock_pick_id = stock_pick_obj.search(cr, uid, [('origin', '=', move.origin)], context=context)
            stock_pick_obj.write(cr, uid, stock_pick_id, {'min_date': order_ref}, context=context)
        return
