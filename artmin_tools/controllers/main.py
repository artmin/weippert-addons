from geoip import geolite2
from openerp import http
from openerp.http import request

class artmin_tools(http.Controller):
  
  @http.route(['/country_from_ip'], type='http', auth="public", website=True)
  def country_from_ip(self, **post):
    ip = '85.181.243.186'
    match = geolite2.lookup(ip)
    country = match.country
    country_code = request.session['geoip'].get('country_code')
    values = {
            'ip' : ip,
            'country' : country,
            'country_code' : country_code,
            'remote_addr' : request.httprequest.remote_addr,
            }
    return request.website.render("artmin_tools.country_from_ip", values)
    

