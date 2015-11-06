﻿{
    'name': 'Work time analysis report',
    'version': '1.1',
    'category': 'Human Resources',
    'description': 
    """
    Work time analysis report. 
    
    This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions.
    """,
    'depends': [
        'account_analytic_account_improvements',
        'hr_analytic_timesheet_improvements',
    ],
    'data': [
        'wizard/work_time_analysis_view.xml',
        'report/work_time_analysis_report.xml',
    ],
    'installable': True,
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
}