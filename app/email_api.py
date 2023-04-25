import smtplib, ssl, base64

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "firewatchalerts@gmail.com"  # Enter your address
password = base64.b64decode("YmFidXJlbWNubmlianJsaQ==").decode("utf-8")


def send_alerts(items):
    context = ssl.create_default_context()
    message = f"""\
Subject: Low price detected
The following items have been detected under their price threshholds: \n
    """
    for item in items:
        message += f"name: {item[0]}, price: {item[2]}, url: {item[1]} \n"

    email_list = ["sougioulkos@gmail.com"]
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        for email in email_list:
            server.login(sender_email, password)
            server.sendmail(sender_email, email, message)
