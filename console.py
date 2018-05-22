#!/usr/bin/python

'''
alpha-framework console build 2
version 0.2.3 | 2018 base

made with love in python
'''

import sys, time, os, urllib2

id = ''
fno = ''
username = ''

print 'Welcome to alpha-framework'
while True:
    cmd = raw_input('alpha$ ')
    if cmd == 'set_id':
        print 'Setting auth id...'
        id = raw_input('id: ')
    elif cmd == 'config':
        print 'printing config...'
        print 'id: ', id
        print 'no: ', fno
        print 'user: ', username
    elif cmd == 'set_no':
        print 'Setting follower number...'
        fno = raw_input('no: ')
    elif cmd == 'set_user':
        print 'Setting username...'
        username = raw_input('user: ')
    elif cmd == 'run':
        if id == '' or fno == '' or username == '':
            print 'please configure the requst auth, read readme.txt for help'
        else:
            req = urllib2.urlopen('http://[http_server_ip]/api.php?id=', id, '&fno=', fno, '&username=', username)
            print req.read()
    elif cmd == '':
        temp = 0
    else:
        print 'type help or ? for help lol'
