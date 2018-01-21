__author__ = 'Administrator'
db.define_table('iplist',Field('IPADDR',requires=IS_NOT_EMPTY()),
                Field('VMNAME'),
                Field('STATUS',requires=IS_NOT_EMPTY()),
                auth.signature)
