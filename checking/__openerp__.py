{
    'name':'Checking',
    'category':'Testing',
    'depends':['base','web'],
    "website" : "http://www.rove.de/",
    "image":'/checking/static/img/Internet-Explorer-icon.png',
    'description':"""
    Lets begin 
    
    """,
    'data':[
#             'security/checking_security.xml', 
#             'security/ir.model.access.csv',
            'views/menu.xml',
            'views/checkone.xml',
            'views/emaiiiil.xml',
            'views/number.xml',
            'views/onchange.xml',
            'views/test.xml'
            
    
           ],
           'js': ['static/src/js/function.js'],
           'css': ['static/src/css/checking.css'],
           'qweb': ['static/src/xml/check.xml'],
           
           'icon':'/checking/static/img/Internet-Explorer-icon.png',

}