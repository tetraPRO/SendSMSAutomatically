#!/usr/bin/env python
import smtplib
import csv

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'caputo.philip@gmail.com', 'seryne2012' )

# Send text message through SMS gateway of destination number
message = 'Affordable life insurance to protect your family!\nwww.ineedlifeinsuarancenow.com'

carrierList = {1:'txt.att.net',
               2:'sms.myboostmobil.com',
               3:'sms.mycricket.com',
               4:'mymetropcs.com',
               5:'vtext.com',
               6:'messaging.sprintpcs.com',
               7:'tmomail.net',
               8:'email.uscc.net',
               9:'vmobl.com'}

#open leadList file
with open('/home/capphil1/Documents/r_list_office@bitcoinpaper.money_1520866665.csv', 'rb') as leadFile:
	reader = csv.reader(leadFile)

#iterate through each & every row and send sms text to every number
#trying every carrier option as we do not know which carrier the number
#belongs to.  Takes about 5 or 6 seconds for every number.
	for row in reader:
            print(row[1])
            for carrier in carrierList:
                number = str(row[1]) + '@' + str(carrierList[carrier])
                server.sendmail('Philip', number, message)
                print number
