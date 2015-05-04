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
from openerp import SUPERUSER_ID

class weippert_product(osv.osv):

    _inherit = 'product.template'
    _description = "Custom fields for Weippert products."

    _columns = {
        # Fertigung
        'zeichnung': fields.char('Zeichnung', size=64),
        'alte_zeichnung' : fields.char('Alte Zeichnung', size=64),
        'box' : fields.char('Behälter', size=32),
        'box_menge' : fields.integer('Behälterinhalt', size=10),
        'werkzeug_nr' : fields.char('Werkzeugnummer', size=64),
        'verpackungsart' : fields.char('Verpackungsart', size=128),
        'machine_nr' : fields.char('Maschinenbelegung', size=64),
        # Verkauf
        'kontrakt_nr' : fields.char('Kontraktnummer', size=32),
        'kontraktmenge' : fields.integer('Kontraktmenge', size=10),
        'restmenge' : fields.integer('Restmenge', size=10),
    }

weippert_product()

