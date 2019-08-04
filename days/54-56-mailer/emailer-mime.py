#!python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app_pass = input("Enter your Gmail app password:\n")
from_addr = input("Enter the from address:\n")
to_addr = input("Enter the to address:\n")

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'To my best friend'

body = input("Enter the body of the email:\n")

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(from_addr, app_pass)

text = msg.as_string()

smtp_server.sendmail(from_addr, to_addr, text)

smtp_server.close()

print('email sent')
