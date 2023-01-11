# -*- coding: utf-8 -*-
{
    "name": "Kitamaju Theme",
    "summary": """
        Kitamaju.id - Theme""",
    "description": """
        Kitamaju.id - Theme
    """,
    "author": "ERP Indonesia",
    "website": "https://erpindonesia.co.id",
    "category": "Others",
    "license": "LGPL-3",
    "version": "15.0.1",
    "depends": [
        "website",
    ],
    "assets":{
        'web._assets_primary_variables': [
            ('prepend','kitamaju_theme/static/src/scss/theme_style.scss'),
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}
