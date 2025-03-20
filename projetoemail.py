import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtp_server = 'smtp.gmail.com'
smtp_port = 587

email_address = 'thalesgabriel536@gmail.com'
senha = 'wakr vghg sgxs nmay'

sender_email = email_address
receiver_email = 'geovannacaroline1516@gmail.com'
assunto = 'MENSAGEM DO SEU AMOR'
body = 'TO BRAVO COM VC @-@ MAS EU TE AMO HM'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = assunto

message.attach(MIMEText(body,'plain'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_address,senha)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email enviado com sucesso')