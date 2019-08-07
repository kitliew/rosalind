import smtplib
import datetime

current = datetime.datetime.now()

To_who = "liewkitxi_1993@hotmail.com"
Subject = "Testing email using Python"      #this format can't attach subject
msg_content = "\n Here is where you should type your msg"   #need to put \n in front

sender_email = "Kit.Liew@rhul.ac.uk"
email_password = "transformation"

server = smtplib.SMTP("smtp.office365.com", 587)
server.ehlo()
server.starttls()
server.login(sender_email, email_password)
server.sendmail(sender_email, To_who, msg_content)
print("Email sent" + " " + str(current))
server.quit()
