
from typing import NoReturn

from environ import Env
from mailjet_rest import Client

# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.infrastructure.environ import DjangoEnviron
# Domain
from modules.shared.domain.email import EmailSender


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class MailjetEmailSender(EmailSender):
    """
    Mailjet Send Email
    """

    def __init__(self, client=None, environ=None):
        self.__environ = environ or DjangoEnviron()
        mailjet_apikey_public = self.__environ.get('MAILJET_APIKEY_PUBLIC')
        mailjet_apikey_private = self.__environ.get('MAILJET_APIKEY_PRIVATE')

        if mailjet_apikey_private is None:
            raise Exception(f"MAILJET_APIKEY_PUBLIC is not "
                            f"properly configured {mailjet_apikey_public}")

        if mailjet_apikey_private is None:
            raise Exception(f"MAILJET_APIKEY_PRIVATE is not "
                            f"properly configured {mailjet_apikey_private}")

        auth = (
            mailjet_apikey_public,
            mailjet_apikey_private
        )
        self.__mailjet_client = client or Client(auth=auth)

    def send(self, sender_email: str, recipient_email: str, subject: str = '', message: str = '') -> NoReturn:
        """
        Send email
        @param sender_email: sender email
        @type sender_email: str
        @param recipient_email: recipient email
        @type recipient_email: str
        @param subject: subject
        @type subject: str
        @param message: message
        @type message: str
        @return: NoReturn
        @rtype: NoReturn
        """
        mail_data = {
            'FromEmail': sender_email,
            'FromName': sender_email,
            'Subject': subject,
            'Html-part': message,
            'Recipients': [{'Email': recipient_email}]
        }
        response = self.__mailjet_client.send.create(data=mail_data)
        if response.status_code not in [200]:
            raise Exception(f"The mailjet response without status 200, verify {response.content.decode('utf-8')}")

        self.log.info(f"Sent email response: {response.content.decode('utf-8')}")



