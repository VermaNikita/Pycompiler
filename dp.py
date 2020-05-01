#!/usr/bin/python3

import cgi
import subprocess as sb
from os import system
FORM = cgi.FieldStorage()
##HEADERS
print("Content-type: text/html")
print()
ERROR = False
##HTML
html ='''<html><head><title>COMILER: Python</title></head>
        <body><h1> Run Python </h1>
        <form method ="post"
            action="http://localhost/cgi-bin/dp.py">
        <h2>Write your code below:-</h2>
            <textarea name ="code"
            rows =15 cols =30></textarea>
            <input type ="Submit" value="Submit"></input>
        </form></body></html>
'''
print(html)
CODE =FORM["code"].value
print(CODE)
FILE =open('/var/www/html/code/n.py','w')
FILE.write(CODE)
FILE.close()
print('<br>')
print('<br>')
print("\n....Running The Code....")
print('<br>')
print('<br>')
OUT=sb.getoutput("python3 /var/www/html/code/n.py")
print("The output is :- \r\n",OUT)








