import smtplib # This is the SMTP library we need to send the email notification
import os
from dotenv import load_dotenv
load_dotenv()

# Define some variables to be used later on in our script

# You might not need the username and password variable, depends if you are using a provider or if you have your raspberry pi setup to send emails
# If you have setup your raspberry pi to send emails, then you will probably want to use 'localhost' for your smtp_host

smtp_username = os.getenv('GMAIL_USER') # This is the username used to login to your SMTP provider
smtp_password = os.getenv('GMAIL_PASS') # This is the password used to login to your SMTP provider
smtp_host = "smtp.gmail.com" # This is the host of the SMTP provider
smtp_port = 465 # This is the port that your SMTP provider uses

smtp_sender = smtp_username # This is the FROM email address

smtp_receivers = os.getenv('NOTIFICATION_RECEIVERS').split(',') # This is the TO email address
message_template = """\
From: %s
To: %s
Subject: WaterBot Notification

""" % (smtp_sender, ", ".join(smtp_receivers))

# This is our sendEmail function

def sendEmail(smtp_message):
	try:
		email = message_template + smtp_message
		server = smtplib.SMTP_SSL(smtp_host, smtp_port)
		server.ehlo()
		server.login(smtp_username, smtp_password) # If you don't need to login to your smtp provider, simply remove this line
		server.sendmail(smtp_sender, smtp_receivers, email)         
		print ("Successfully sent email" + "\n"+ email)
		server.close()
	except smtplib.SMTPException:
		print ("Error: unable to send email"+ "\n"+ email)

def send(message):
    # print (message)
    sendEmail(message)