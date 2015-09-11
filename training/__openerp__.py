{
    'name':'Training details',
    'category':'register',
    'depends':['base'],
    "website" : "http://www.rove.de/",
    
    'description':"""
    Its begin 
    'image'::'/opt/odoo/trial_modules/training/tan.png,
    Training details for freshers
    """,
    'data':[
#             'data/demo_data.xml',
            'views/menu.xml',
            'views/show.xml',
            'views/question.xml',
            'views/ransearch.xml',
            'views/inheritts.xml',
            'views/comp.xml',
            'views/inherit2.xml',
            'views/dele1.xml',
            'views/dele2.xml',
            'views/dele3.xml',
            'views/viewlevel.xml',
            'views/constraints.xml',
            'views/dele4.xml',
            'views/sample.xml',

           ],
   
    
     'active':True,
    'installable': True
    

}