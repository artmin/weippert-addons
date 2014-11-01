{
    'name': 'dreh24 Shop',
    'category': 'Website',
    'summary': 'Shop alterations for dreh24 AG',
    'version': '1.0',
    'description': """
Changes in shop for company dreh24 AG. E.g. showing the Sales Unit Price instead
of the list price.
        """,
    'author': 'IT - artmin',
    'depends': ['product','website_sale'],
    'data': [
        'views/dreh24_shop.xml',
        'views/dreh24_pages.xml',
        'product_view.xml',
    ],
    'installable': True,
    'auto-install' : False,
}
