# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Ecosoft Co., Ltd. (http://ecosoft.co.th).
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

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp

class product_product(osv.osv):

    _inherit = "product.product"
    _columns = {
        'uom_so_id': fields.many2one('product.uom', 'Verpackungseinheit',
            required=False, help="Mengeneinheit für Verkäufe. Muss in " +
            "der gleichen Mengeneinheit sein, wie Standardmengeneinheit."),
    }
    
    def _check_so_uom(self, cursor, user, ids, context=None):
        for product in self.browse(cursor, user, ids, context=context):
            if product.uom_so_id and (product.uom_id.category_id.id <> product.uom_so_id.category_id.id):
                return False
        return True
        
    _constraints = [
        (_check_so_uom, 'Error: The default Unit of Measure and the sales Unit of Measure must be in the same category.', ['uom_id']),
    ]
       
product_product()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
