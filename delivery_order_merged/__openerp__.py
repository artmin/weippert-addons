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
{
    'name': 'Merge Delivery Order',
    'version': '1.0',
    'category': 'Stock',
    'description': """
        Merge Delivery Order.
        
        
        This Module will check following condition while merging delivery order
        
        
        1. Delivery Order should be in same state
        
        2. Delivery Order should be in same Invoice State
        
        3. Delivery Order should be in same Customer
        
        
        
        You will find the merge delivery Order Wizard in More option above the Tree View
        
        For More Reference::
        
        http://maheshwarimayur.blogspot.in/2014/06/how-to-merge-delivery-order-in-openerp.html
        
        
    """,
    'author': 'Mayur Maheshwari',
    'website':'http://maheshwarimayur.blogspot.in',
    'depends': ['purchase','stock','sale'],
    'init_xml': [],
    'update_xml': [
        'wizard/incoming_shipment_merge_view.xml',
    ],
    'demo_xml': [
    ],
    'test':[
    ],
    'installable': True,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
