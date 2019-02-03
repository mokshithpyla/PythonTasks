#Sending Email using Python

import smtplib 

#create SMTP object - server
server=smtplib.SMTP('smtp.gmail.com',587) 

#Identify yourself to an ESMTP server using EHLO
#Put the SMTP connection in TLS (Transport Layer Security) mode to ensure encryption and Call ehlo again

server.ehlo() 
server.starttls()
server.ehlo()

#importing required modules 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#composing some of the basic message headers:

fromaddr = "firstinternforxpms@gmail.com"
toaddr = "mokshithpyla@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"
body = "Python test mail"

#attach the body of the email to the MIME message:

msg.attach(MIMEText(body, 'plain'))

#login with matching credentials

server.login("firstinternforxpms@gmail.com", "xxxxxxxxxx")

#For sending the mail, we have to convert the object to a string

text = msg.as_string()

#Finally, sending the email:

server.sendmail(fromaddr, toaddr, text)
