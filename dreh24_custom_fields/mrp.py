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

class weippert_mrp(osv.osv):

    _inherit = 'mrp.bom'
    _description = "Custom fields for Weippert bill of material."

    _columns = {
        'farbe': fields.char('Farbe zu Material', size=64),
    }

weippert_mrp()

class weippert_mrp_bom_line(osv.osv):
    _inherit = 'mrp.bom.line'
    _description = "Additional column for intern and extern products."

    _columns = {
        'workcenter_id' : fields.many2one('mrp.workcenter', 'Arbeitsplatz'),
    }
weippert_mrp_bom_line()

class weippert_mrp_coworker(osv.osv):
    _name = 'mrp.coworker'
    _description = 'Coworker who is responsible for routing.'

    _columns = {
        'name' : fields.char('Bearbeiter'),
        }
weippert_mrp_coworker()

class weippert_mrp_routing_workcenter(osv.osv):
    _inherit = 'mrp.routing.workcenter'
    _description = "Add coworker to routing"

    _columns = {
        'coworker_id' : fields.many2one('mrp.coworker', 'Bearbeiter')
        }
weippert_mrp_routing_workcenter()

class weippert_mrp_production_workcenter_line(osv.osv):
    _inherit = 'mrp.production.workcenter.line'
    _description = "Add coworker to production line"

    _columns = {
            'coworker_id' : fields.many2one('mrp.coworker', 'Bearbeiter')
            }
weippert_mrp_production_workcenter_line()

class weippert_mrp_bom(osv.osv):
    _inherit = 'mrp.bom'
    _description= "Make sure coworkers are copied to production workcenter lines."

    "Override method"
    def _bom_explode(self, cr, uid, bom, product, factor, properties=None,
            level=0, routing_id=False, previous_products=None, master_bom=None,
            context=None):
        res_product, res_work = super(weippert_mrp_bom, self)._bom_explode(
                cr, uid, bom,
                product, factor, properties=properties, level=level,
                routing_id=routing_id, previous_products=previous_products,
                master_bom=master_bom)
        routing_obj = self.pool.get('mrp.routing')
        routing = (routing_id and routing_obj.browse(cr, uid, routing_id) or
                bom.routing_id or False)
        if routing:
          for line in res_work:
            # Find routing line with same id and copy coworker
            for wc_use in routing.workcenter_lines:
              if line['workcenter_id'] == wc_use.workcenter_id.id:
                line.update({ 'coworker_id' : wc_use.coworker_id.id })
        return res_product, res_work
