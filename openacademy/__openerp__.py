#
# Open Academy manifest file
#
{
    'name': 'Open Academy test',
    'category': 'Test',
    'version': '1.0',
    'author': 'Me',
    'depends': ['base','website'],

    'description': """
Open Academy module for managing trainings:
 - training courses
 - training sessions
 - attendee registration
""",
    'data': [
        'views/menu.xml',
        'views/course.xml',
        'views/session.xml',
        'views/wiz_session.xml',
        'views/simple_template.xml',
        'views/snippet.xml',
        'reports/report_session.xml',
    ],
}
