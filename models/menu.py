# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
response.logo = A(B('My first app'),XML('&NBSP;'),
                  _class="brand",_href="http://www.web2py.com/")
response.menu = [
    (T('Home'), False, URL('default','index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('My Sites'), False,'#',[
            (T('Query'), False, URL('default', 'index')),
            (T('RegIP'), False, URL('default', 'regip'))
        ])
    ]

