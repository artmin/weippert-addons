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

    _inherit = 'sale.order'
    _columns = {
        'client_order_ref_date': fields.date('Ihr Schreiben vom', select=1,
            help="Datum der Anfrage des Kunden"),
        'custom_delivery_date': fields.date('Wunschtermin Lieferung', select=1,
            help="Vom Kunden gewünschtes Datum für die Lieferung des Auftrages"),
    }
    
    _defaults = {           
        'client_order_ref_date' : fields.datetime.today(), 
    }
