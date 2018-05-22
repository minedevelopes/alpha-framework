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
    elif cmd == '?' or 'help':
        print 'displaying alpha-framework help'
        print '? or help | to show this box'
        print 'set_id | to set the auth id'
        print 'set_no | to set the follower number [ cant be less than 500 and more than 600]'
        print 'set_user | to set the username'
        print 'run | to send the followers and to use this command you need to run the 3 commands above'
        print 'config | to show the current configurations'
    elif cmd == 'config':
        print 'printing config...'
        print 'id: ', id
        print 'no: ', fno
        print 'user: ', username
    elif cmd == 'set_no':
        print 'Setting follower number...'
        id = raw_input('no: ')
    elif cmd == 'set_user':
        print 'Setting username...'
        id = raw_input('user: ')
    elif cmd == 'run':
        if id == '' or fno == '' or username == '':
            print 'please configure the requst auth, type help or ?'
        else:
            req = urllib2.urlopen('http://[http_server_ip]/api.php?id=', id, '&fno=', fno, '&username=', username)
            print req.read()
    elif cmd == '':
        temp = 0
    else:
        print 'type help or ? for help lol'
