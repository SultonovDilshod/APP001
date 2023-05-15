import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user = "halimovhalimjon420@gmail.com"
    password_app = "uffiduknjivzwskm"
    receiver = "sultonovdilshodaka@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password_app)
        server.sendmail(user, receiver, message)
