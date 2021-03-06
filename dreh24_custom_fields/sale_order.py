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
from datetime import datetime

class dreh24_sale_order(osv.osv):

    def _first_product(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        # Get first product of sales order
        for sale_order in self.browse(cr, uid, ids, context=None):
          if sale_order.order_line and len(sale_order.order_line) > 0:
            #line_obj = self.pool.get('sale.order.line')
            #line = line_obj.browse(cr, uid, sale_order.order_line[0])
            res[sale_order.id] = sale_order.order_line[0].name
          else:
            res[sale_order.id] = ''
        return res
    
    _inherit = 'sale.order'
    _columns = {
        'client_order_ref_date': fields.date('Ihr Schreiben vom', select=1,
            help="Datum der Anfrage des Kunden"),
        'custom_delivery_date': fields.date('Wunschtermin Lieferung', select=1,
            help="Vom Kunden gewünschtes Datum für die Lieferung des Auftrages"),
        # Is needed for table view of sales orders
        'first_product' : fields.function(
            _first_product,
            type="char",
            string="Artikel"),
        }    
    
    _defaults = {           
        'client_order_ref_date' : fields.date.today(), 
    }

    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        res = super(dreh24_sale_order, self).onchange_partner_id(cr, uid,
                ids, part, context=context)
        vals = res['value']
        partner_obj = self.pool.get('res.partner').browse(cr, uid, part)
        if partner_obj.incoterm:
          vals['incoterm'] = partner_obj.incoterm
        else:
          vals['incoterm'] = False
        return {'value' : vals }
