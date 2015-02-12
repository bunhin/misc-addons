{
    'name' : 'Autopay in eCommerce',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Custom',
    'website' : 'https://it-projects.info',
    'description': """
After customer make an online payment (e.g. via paypal), new invoice is created and validated.

Tested on Odoo 8.0 f8d5a6727d3e8d428d9bef93da7ba6b11f344284
    """,
    'depends' : ['website_sale', 'payment'],
    'data':[
        'views.xml',
        ],
    'installable': True
}
