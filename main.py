import smtplib
import string
BODY= ((
    "From %s" % 'praiseland2023@gmail.com',
     "To %s" % 'hanushiv2020@gmail.com',
      "Subject %s" % 'Test mail',
      "",'this is a test mail'
    
),"\r\n")

server=smtplib.SMTP('smtp.gmail.com',587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login('praiseland2023@gmail.com','Martha#9978')
server.sendmail('praiseland2023@gmail.com',['hanushiv2020@gmail.com'],BODY)
server.quit()
"""

message="hello"

print("Mail sent")
server.quit()

"""