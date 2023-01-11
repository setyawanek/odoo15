{
    'name': "Kitamaju Admission",
    'version': '15.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    'sequence': 3,
    'summary': "Manage Admissions""",
    'complexity': "easy",
    'author': 'Kitamaju',
    'website': 'https://erpindonesia.co.id/',
    'depends': [
        'base',
        'openeducat_core',
        'openeducat_fees',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/admission_sequence.xml',
        'views/admission_register_view.xml',
        'views/admission_view.xml',
        'report/report_admission_analysis.xml',
        'report/report_menu.xml',
        'wizard/admission_analysis_wizard_view.xml',
        'menus/op_menu.xml',
    ],
    'demo': [
        'demo/admission_register_demo.xml',
        'demo/admission_demo.xml',
    ],
    'test': [],
    'images': [
        'static/description/openeducat_admission_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
