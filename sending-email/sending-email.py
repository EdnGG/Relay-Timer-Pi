import smtplib
# from decouple import config

message = 'hello from Raspberry Pi'
subject = 'Testing e-mail'

message = 'Subject: {}\n\n{}'.format(subject,message) 

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('gresseden@gmail.com', '!!!2885GogE')

server.sendmail('gresseden@gmail.com', 'gresseden@gmail.com ', message )


server.quit()

print('correo enviado successfull')