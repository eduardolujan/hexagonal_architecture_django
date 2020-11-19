
from typing import NoReturn

from environ import Env
from mailjet_rest import Client

# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.infrastructure.environ import DjangoEnviron
# Domain
from modules.shared.domain.email import SendEmail


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class MailjetSendEmail(SendEmail):
    """
    Mailjet Send Email
    """

    def __init__(self, client=None, environ=DjangoEnviron()):
        self.__environ = environ
        mailjet_apikey_public = self.__environ.get('MAILJET_APIKEY_PUBLIC')
        mailjet_apikey_private = self.__environ.get('MAILJET_APIKEY_PRIVATE')

        if mailjet_apikey_private is None:
            raise Exception(f"MAILJET_APIKEY_PUBLIC is not set {mailjet_apikey_public}")

        if mailjet_apikey_private is None:
            raise Exception(f"MAILJET_APIKEY_PRIVATE is not set {mailjet_apikey_private}")

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
        try:
            mail_data = dict(
                Messages=[
                    dict(
                        From=dict(
                            Email=f"{sender_email}",
                            Name=f"{sender_email}"
                        ),
                        To=dict(
                            Email=f"{sender_email}",
                            Name=f"{sender_email}"
                        ),
                        Subject=subject,
                        HTMLPart=message
                    )
                ]
            )
            self.__mailjet_client.send.create(data=mail_data)
        except Exception as err:
            self.log.exception(f"Error in Mailjet::send, err:{err}")
