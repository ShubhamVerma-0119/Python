# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:47:51 2020

@author: Shubham Verma
"""
import getpass 
import smtplib
from email.message import EmailMessage

email = EmailMessage()

to = input("To: ")
subject = input("Subject: ")
Content = input("Content: ")
Your_EmailID = input("Your email ID: ")
Your_password = getpass.getpass(prompt='Password: ', stream=None)
name = input("Enter Your Name: ")

email['from'] = name
email['to'] = to
email['subject'] = subject

email.set_content(Content)

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Your_EmailID, Your_password)
    smtp.send_message(email)
    print('Mail has sent!')
