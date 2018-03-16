import smtplib

mailer=smtplib.SMTP_SSL('imap.gmail.com')
mailer.login('singhsomesh0@gmail.com','themorningstar')
mailer.sendmail('singhsomesh0@gmail.com','somessh247@gmail.com','Subject: Random Shit Again \n\n dont bother replying again')
mailer.quit()
