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
{
    'name': 'Custom fields Weippert',
    'version': '1.0',
    "category" : 'Partner',
    'complexity': "easy",
    'description': """
Custom fields Weippert
===========================

* Automatisch vergebene interne Referenzen
* Kunden/Lieferanten-Nr.
* Lieferbedingungen
* Anfragedatum
* Wunschtermin für Lieferung
* Referenz/Beschreibung
* Zusätzliche Felder für Produkte (Fertigung, Kontraktdaten)
* Zusätzliche Felder für Stückliste
* Änderung Ansicht für Produkte und Aufträge

    """,
    'author': 'artmin - IT-Dienstleistungen',
    'website': 'http://it.artmin.de',
    'depends': ['sale','product','stock','account','delivery'],
    'data': ['partner_sequence.xml',
        'partner_ref_view.xml',
        'sale_order_view.xml',
        'product_view.xml',
        'mrp_view.xml',
        'security/ir.model.access.csv',
        'stock_view.xml'],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
