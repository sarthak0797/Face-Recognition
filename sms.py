from twilio.rest import Client
import socket
import sys
import smtplib
from smtplib import SMTP as SMTP 

# Find these values at https://twilio.com/user/account
account_sid = "AC219841d7fccf7db276422e6944685410"
auth_token = "cdfacb6a28347c34007b12259676d40a"

client = Client(account_sid, auth_token)

def msg():
	client.api.account.messages.create(
	    to="+918979518980",
	    from_="4172655285",
	    body="zvzcx")


def mail1(msg,email):
	print(msg.encode("utf-8"))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	#Next, log in to the server
	server.login("sarthak.kohli.0.7@gmail.com", "8979518980")

	#Send the mail
	msg = msg
	server.sendmail("sarthak.kohli.0.7@gmail.com", email, msg.encode("utf-8"))