def Send_mail(message):
    import smtplib
    import ssl
    host = "smtp.gmail.com"
    port = 465
    username = "ykrishan9063@gmail.com"
    password = "gsupftfkhyzchqml"
    receiver = "ykrishan9063@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

