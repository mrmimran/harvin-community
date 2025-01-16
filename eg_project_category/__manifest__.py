{
    'name': 'Project Category',
    'version': '17.0',
    'category': 'Project',
    'summary': 'This app will project category.',
    'author': 'INKERP',
    'website': "http://www.inkerp.com/",
    'depends': ['project'],

    'data': [
            'views/project_project_view.xml',
            'views/project_category_view.xml',
            'security/ir.model.access.csv',
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
