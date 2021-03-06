{
    'name': 'dreh24 Reports',
    'category': 'Report',
    'summary': 'Reports for dreh24 AG',
    'version': '1.0',
    'description': """
Reports for company dreh24 AG
        """,
    'author': 'IT - artmin',
    'depends': ['product_so_uom',
        'website_sale_delivery',
        'dreh24_custom_fields'],
    'data': [
        'views/dreh24_layout.xml',
        'views/dreh24_reports.xml',
        'views/weippert_production_report.xml',
        'views/mrp_delivery.xml',
        'mrp_delivery_report.xml',
    ],
    'installable': True,
    'auto-install' : False,
}
