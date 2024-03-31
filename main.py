# отправка письма на почту через gmail и python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    # Заполните эти поля вашими данными
    sender_email = "почта, с которой отправляют"  # gmail почта, к которой привязан пароль приложения
    receiver_email = "почта, кому отправить"  # кому
    password = "пароль приложения"  # пароль приложения (в gmail получил в разделе безопасность - пароль приложений)
    subject = "Subject of the email"
    body = 'text message'  # текст сообщения

    # Создание объекта сообщения
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Добавление тела письма
    message.attach(MIMEText(body, 'plain'))

    # Создание объекта сессии SMTP
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Укажите здесь свой SMTP сервер
    session.starttls()  # Активация шифрования
    session.login(sender_email, password)  # Авторизация на сервере

    # Отправка сообщения
    session.sendmail(sender_email, receiver_email, message.as_string())
    session.quit()

    print("Email sent successfully.")


send_email()
