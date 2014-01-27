#!python
import cgi,cgitb
cgitb.enable()
print(content-type:text/html")
print("  ")
f=cgi.Fieldstorage()
n=f.getvalue('uname')
print("Hi{0},welcome to python".format(n))
