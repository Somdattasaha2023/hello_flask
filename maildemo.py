import smtplib
import os,sys
"""
server=smtplib.SMTP('smtp.gmail.com',587)
#server.connect('smtp.gmail.com',465)
server.ehlo()
server.starttls()
server.ehlo()
try:
    server.login('praiseland2023@gmail.com','Martha#9978')
    server.sendmail('praiseland2023@gmail.com','hanushiv2020@gmail.com','BODY')
except Exception :
        print(Exception)
print('mail sent')

SCRIPT_NAME = "C:\\Users\\User\\hello_flask\\aaa.py"


#C:\Users\User\hello_flask
print(os.sep)
NAME1 = ".".join(SCRIPT_NAME.split(os.sep)[-1].split(".")[0:-1])
NAME = ".".join(SCRIPT_NAME.split(os.sep)[-1].split(".")[0:-1])

print(str(NAME ))
#print(NAME1)

"""