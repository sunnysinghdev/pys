#!C:/Users/Sunny.Singh/AppData/Local/Programs/Python/Python36
import os
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print("Content-type: text/html")
print("")
print("<html><head>")
print("")
print("</head><body>")
print("<font size=+1>Environment</font></br>")
for param in os.environ.keys():
   print("<b>%20s</b>: %s</br>" % (param, os.environ[param]))
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("<button href='download.py'> Download </button>")
print("</body></html>")
