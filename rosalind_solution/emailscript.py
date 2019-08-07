import datetime                                     #to know what time sent
from email.mime.multipart import MIMEMultipart      #email format from,to,Subject
from email.mime.text import MIMEText
import smtplib

current_time = datetime.datetime.now()

msg= MIMEMultipart()

email_password = "transformation"                   #sender email email_password

msg["From"] = "Kit.Liew@rhul.ac.uk"                 #sender email
msg["To"] = "liewkitxi_1993@hotmail.com"            #to who?
msg["Subject"] = "Type subject here"

body = "Type your message here!"
msg.attach(MIMEText(body))
print(msg)

server = smtplib.SMTP("smtp.office365.com", 587)    #server name, port number
server.ehlo()
server.starttls()
server.login(msg["From"], email_password)
server.sendmail(msg["From"], msg["To"], msg.as_string())

print("Email sent" + " " + str(current_time))

server.quit()
