from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.utils.timezone import localdate

from chalets.models import Subscription

subscriptions = Subscription.objects.filter(is_approved=True)
for subscription in subscriptions:
    if subscription.subscription_end_date == localdate().today() + relativedelta(days=+ 10):
        send_mail('Subscription Alert',
                  'Your subscription after 10 days will be ended, this is a simple reminder',
                  'info@qassimchalets.com',
                  [subscription.user.email])