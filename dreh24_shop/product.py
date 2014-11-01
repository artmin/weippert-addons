from openerp.osv import osv, fields
import openerp.addons.decimal_precision as dp

class product_template(osv.Model):
  _inherit = "product.template"
  _name = "product.template"

  _columns = {
          'list_price_ch' : fields.float('Verkaufspreis CH', type='float',
              digits_compute=dp.get_precision('Product Price')),
          }
