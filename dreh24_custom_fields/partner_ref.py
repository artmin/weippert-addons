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
    _description = "Automatische Vergabe von Kundennummern"

    _columns = {
        'your_ref' : fields.char('Kunden/Lieferanten-Nr.', size=64),
        'incoterm' : fields.many2one('stock.incoterms', 'Lieferbedingung'),
    }
    
    _defaults = {           
        'customer' : lambda self, cr, uid, context : context['customer'] if context and 'customer' in context else 1,
        'supplier' : lambda self, cr, uid, context : context['supplier'] if context and 'supplier' in context else 0, 
    }
    
    def create(self, cr, uid, vals, context=None):
        # Only assert partner references to "real" customers not contacts and if
        # reference ha not been entered manually already
        if not vals.get('parent_id') and not vals.get('ref'):
            # Get company id from vals if available
            if vals.get('company_id'):
              company = self.pool.get('res.company').browse(cr, uid, vals['company_id'], context=context)
            # If no company is set, get company from user    
            else:
              user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
              company = self.pool.get('res.company').browse(cr, uid, user.company_id.id, context=context)
            # Construct customer reference according to company
            if company.name:
              # Get sequence
              if company.name == 'dreh24 AG':
                ref = self.pool.get('ir.sequence').get(cr, uid, 'partner.ref.dreh24')
                vals['ref'] = 'D' + str(ref)
              else:
                ref = self.pool.get('ir.sequence').get(cr, uid, 'partner.ref.weippert')
                vals['ref'] = 'W' + str(ref)
        return super(artmin_partner_reference, self).create(cr, uid, vals, context=context)

artmin_partner_reference()
