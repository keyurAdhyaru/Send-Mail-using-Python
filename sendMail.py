import smtplib 
sm = smtplib.SMTP('smtp.gmail.com',587)
sm.starttls()	#start serivce.
#login to the mail id.
sm.login("Sender Id","Password")
#send mail.
sm.sendmail("Sender Id","Recivers Id","Message")
sm.quit()	#Stop serivce.