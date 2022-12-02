from app import db
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version


class ModelMixin(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class MailSend(object):

    def send_email(message):
        # server = 'smtp.gmail.com'
        # user = 'saliwanm@gmail.com'
        # password = 'password'

        recipients = ['saliwanm@gmail.com']
        sender = 'saliwanm@gmail.com'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Password recovery'
        msg['From'] = 'Python script <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(message, 'plain')

        msg.attach(part_text)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()