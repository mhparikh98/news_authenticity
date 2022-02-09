import logging
from celery import Task
from news_authenticity import celery_app
from users.models import (
    User
)
from news_feed.services.send_email_service import SendEmailService

logger = logging.getLogger("news_authenticity")


class SendNotificationEmail(Task):

    name = "send_notification_email"

    def run(self, category):
        """
        Celery task to send the email to the user regarding the news
        """
        try:
            user_profiles = User.objects.filter(preferences__isnull=False)
            users = user_profiles.filter(preferences__name=category)

            for user in users:
                if user.email:
                    SendEmailService.send_email(user.email, user.username, category)
        except Exception as e:
            logger.error(
                dict(
                    message="error while send notification email ",
                    class_name="SendNotificationEmail",
                    errors=e,
                )
            )


send_notification_email = celery_app.register_task(SendNotificationEmail())
