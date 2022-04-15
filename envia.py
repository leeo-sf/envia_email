from string import Template
from datetime import datetime
from dados import email, senha
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


de = "Remetente"
para = "destinatário"


with open("template.html", "r") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.substitute(nome="Destinatário", data=data_atual, linguagem="Python", remetente=de)


msg = MIMEMultipart()
msg["from"] = de
msg["to"] = para
msg["subject"] = "Teste de envio de e-mail."

corpo = MIMEText(corpo_msg, "html")
msg.attach(corpo)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, senha)
    smtp.send_message(msg)

    print("E-mail enviado com sucesso.")

