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

class artmin_partner_reference(osv.osv):

    _inherit = 'res.partner'
    _description = "artmin - partner reference"

    _columns = {
        'ref': fields.char('Referenz', size=64, select=1, readonly=True),
    }
    
    _defaults = {           
        'customer' : lambda self, cr, uid, context : context['customer'] if context and 'customer' in context else 1,
        'supplier' : lambda self, cr, uid, context : context['supplier'] if context and 'supplier' in context else 0, 
    }
    
    def create(self, cr, uid, vals, context=None):
        if not 'ref' in vals:
          # Get sequence
          ref = self.pool.get('ir.sequence').get(cr, uid, 'artmin.partner.ref')
          # Get company id from from if available
          if vals.get('company_id'):
            company = self.pool.get('res.company').browse(cr, uid, vals['company_id'], context=context)
          # If no company is set, get company from user    
          else:
            user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
            company = self.pool.get('res.company').browse(cr, uid, user.company_id.id, context=context)
          # Construct customer reference according to company
          if company.name:
            if company.name == 'dreh24 AG':
              vals['ref'] = 'D' + str(ref)
            elif company.name == 'Weippert Kunststofftechnik GmbH & Co. KG':
              vals['ref'] = 'W' + str(ref)
            else:
              vals['ref'] = 'N' + str(ref)
          else:
            vals['ref'] = 'N' + str(ref)
        return super(artmin_partner_reference, self).create(cr, uid, vals, context=context)

artmin_partner_reference()
