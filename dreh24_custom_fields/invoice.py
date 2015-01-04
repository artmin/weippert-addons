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

from openerp import models, fields, api, _
class account_invoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    # Override validate function
    @api.multi
    def invoice_validate(self):
      # get products object
      product_objs = self.pool.get('product.product')
      uom_objs = self.pool.get('product.uom')
      for line in self.invoice_line:
        if product_objs:
          product = product_objs.browse(self._cr, self._uid, line.product_id.id)
          uos = uom_objs.browse(self._cr, self._uid, line.uos_id.id)
          # Verkaufsmenge von Restmenge abziehen
          if product and product.kontrakt_nr != '':
            quantity = line.quantity * uos.factor_inv
            restmenge = product.restmenge - quantity
            product_objs.write(self._cr, self._uid, line.product_id.id, { 'restmenge' :
              restmenge })
      return super(account_invoice, self).invoice_validate() 
