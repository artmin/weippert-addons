# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

import time
from lxml import etree

from openerp.osv import fields, osv

class sale_order_line(osv.osv):
    
    _inherit = "sale.order.line"
    
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        context = context or {}
        
        res = super(sale_order_line, self).product_id_change(cr, uid, ids, pricelist, product, qty=qty,
            uom=uom, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
            lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, fiscal_position=fiscal_position, flag=flag, context=context)

        # Getting sales uom of product
        if product:
            product = self.pool.get('product.product').browse(cr, uid, product, context=context)
            if product.uom_so_id and not context.get('is_uom_change'):
                res.get('value').update({'product_uom': product.uom_so_id.id})

            # If Sales Unit Price of this Sales UOM is used, use it instead of standard unit price.
            if res.get('value').get('product_uom') or uom == product.uom_so_id.id:
                # Dirty hack: If unit price is equal to list_price and sales uom
                # is not equal to product uom, there must be something wrong.
                # Therefore recalculate!
                
                # Differentiate between swiss and eu prices
                pricelist_obj = self.pool('product.pricelist').browse(cr, uid, pricelist, context=context)
                if pricelist_obj.currency_id.name == 'CHF':
                  list_price = product.list_price_ch
                else:
                  list_price = product.list_price
                  
                # Check if price was calculated properly and correct, if not
                if (res.get('value').get('price_unit') - list_price < 0.01) and \
                  not res.get('value').get('product_uom') == product.uom_id.id:
                  # Calculate price from uom_so_id factor
                  price_computed = product.uom_so_id.factor_inv * res.get('value').get('price_unit') / product.uom_id.factor_inv
                  res.get('value').update({'price_unit': price_computed })            
        return res
    
sale_order_line()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
