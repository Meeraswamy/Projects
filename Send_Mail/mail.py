# Python code to Sending mail from your Gmail account
# You should enable "Send Mail from Third-party apps" option to send mail.
import smtplib

# creates SMTP session
#smtp.gmail.com is the Gmail server to send gmails using
#third party email clients
session = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
# It Puts the SMTP connection in TLS mode
# All SMTP commands that follow will be encrypted
session.starttls()

# Authentication
sender_email_id = input("Enter sender email ID : ")
sender_email_id_password = input("Enter sender email id password : ")
receiver_email_id = input("Enter receiver email ID : ")
# login to SMTP server using Gmail credentials
session.login(sender_email_id,sender_email_id_password)

# message to be sent
message = input("Message_you_need_to_send : ")

# sending the mail
# sends mail to receiver email ID
session.sendmail(sender_email_id,receiver_email_id,message)

# terminating the session
# we should close our session.
session.quit()

print("Email Sent..... ")
