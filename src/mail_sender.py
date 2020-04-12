"""
version : v1.0.0

MIT License

Copyright (c) 2020 Dropper Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
from logging.handlers import RotatingFileHandler

import time

import smtplib
from email.mime.text import MIMEText

import mail_property

logging.Formatter.converter = time.gmtime
logger = logging.getLogger(__name__)
fileHandler = RotatingFileHandler('./log/mail_sender.log', maxBytes=1024 * 1024 * 1024 * 9, backupCount=9)
fileHandler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)s] >> %(message)s'))
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
logger.info('every package loaded and start logging')


def send_mail(origin=mail_property.mail_address, target=mail_property.mail_address, subject='', message=''):
    logger.info('send_mail: function started | origin=' + str(origin) + ' | target=' + str(target) + ' | subject=' + str(subject) + ' | message=' + str(message))

    smtp = smtplib.SMTP_SSL(mail_property.address, mail_property.port)
    smtp.ehlo()
    smtp.login(mail_property.username, mail_property.password)
    logger.info('send_mail: connect and log-in to mail server with SMTP_SSL | smtp=' + str(smtp))

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = origin
    msg['To'] = target
    logger.info('send_mail: make message content | msg=' + str(msg))

    smtp.sendmail(origin, target, msg.as_string())
    logger.info('send_mail: mail sent')

    smtp.quit()
    logger.info('send_mail: smtp connection closed')

    logger.info('send_mail: function ended')
