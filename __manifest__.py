{
    'name': 'Hospital Management System (HMS)',
    'summary': 'Hospital management module for Odoo',
    'version': '1.0',
    'category': 'Healthcare',
    'author': 'Otman Fakri',
    'website': 'Otmanfakri.me',
    'depends': ['base' , 'mail'],
    'data': [
        'views/hms_patient_view.xml',
        'views/hms_patient_menu.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
}
