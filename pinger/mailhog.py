"""
mailhog.py: module to ping Mailhog
"""
import smtplib
from email.mime.text import MIMEText

from clize import run

from pinger.log import logfunc


@logfunc
def mailhog_running(host: str = "localhost", port: int = 1025) -> bool:
    """
    Check if Mailhog is running

    Args
    ----
        host : str, optional, default 'localhost'
        port : str, optional, default '9200'
    """
    smtp_server = smtplib.SMTP(host=host, port=port)
    try:
        message = MIMEText("Ping from Python!")
        message["Subject"] = "Ping from Python!"
        message["From"] = "pinger@localhost"
        message["To"] = "pinger@localhost"

        smtp_server.send_message(message)
        return True
    except smtplib.SMTPException:
        return False
    finally:
        smtp_server.quit()


if __name__ == "__main__":
    run(mailhog_running)
