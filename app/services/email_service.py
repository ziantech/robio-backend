from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import settings
from app.services.email_templates import generate_template


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=True
)

fast_mail = FastMail(conf)


async def send_email(
    subject: str,
    email_to: str,
    body: str | None = None,
    template: str | None = None,
    props: dict | None = None,
    subtype: MessageType = MessageType.html
):
    if template:
        body = generate_template(template, props or {})

    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype=subtype,
    )

    await fast_mail.send_message(message)
