#-*-coding:utf-8-*-
{
    'name': 'Pokedelsx',
    'verson':'0.1',
    'category':'Curso desarrolloOdoo (Pokedex)',
    'description':"""
Cuso desarrollo Odoo (Pokedex)
==============================
    """,
    'depends':[
        'contacts',
        ],
    'data':[
        'security/ir.model.access.csv',
        'views/pokemon_views.xml',
        'views/res_partner_views.xml',
        'wizard/pokemon_evolve_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
