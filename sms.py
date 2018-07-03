from twilio.rest import Client
import socket
import sys
import smtplib
from smtplib import SMTP as SMTP 

# Find these values at https://twilio.com/user/account
account_sid = "**********************"
auth_token = "********************"

client = Client(account_sid, auth_token)

def msg():
	client.api.account.messages.create(
	    to="+91155611415",
	    from_="4172655285",
	    body="zvzcx")


def mail1(msg,email):
	print(msg.encode("utf-8"))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	#Next, log in to the server
	server.login("EMAIL_FROM", "PASSWORD")

	#Send the mail
	msg = msg
	server.sendmail("EMAIL_FROM", email, msg.encode("utf-8"))
