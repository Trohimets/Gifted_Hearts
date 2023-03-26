from datetime import datetime , timedelta
from pandas._libs.tslibs.offsets import relativedelta
from yookassa import Payment,Configuration
from django.core.management.base import BaseCommand
from help_translation.models import AutoPayModel
from core.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from core.settings_ import settings

account_id = settings.ACCOUNT_ID.get_secret_value()
secret_key = settings.SECRET_KEY.get_secret_value()

Configuration.account_id = account_id
Configuration.secret_key = secret_key

class Command(BaseCommand):
    help = 'auto'
    def handle(self, *args, **options):
      to_day = datetime.today().strftime('%Y-%m-%d')
      AutoPayModel.objects.values('uuid').filter(date_next_month__lt=to_day).update(date_next_month=to_day)
      query = AutoPayModel.objects.values('uuid','email','amount').filter(date_next_month=to_day)
      for q in query:
          uuid = q['uuid']
          amount = q['amount']
          payment = Payment.find_one(uuid)
          email_client = q['email']
          payment_saved = payment.payment_method.saved
          if payment_saved == False:
              del_pay = AutoPayModel.objects.filter(uuid=uuid)
              del_pay.delete()
          elif payment_saved == True:
              query_delete = AutoPayModel.objects.filter(uuid=uuid)
              query_delete.delete()
              payment = Payment.create({
                  "amount": {
                      "value": f"{amount}",
                      "currency": "RUB"
                  },
                  "capture": True,
                  "payment_method_id": f"{uuid}",
                  "description": "Автоплатеж"
              })
              uuid = payment.payment_method.id
              date_now = payment.created_at
              date_now = datetime.strptime(date_now, "%Y-%m-%dT%H:%M:%S.%fZ")
              date_now = date_now.date()
              tomorrow = date_now + timedelta(days=1)
              status_money = payment.cancellation_details.reason
              if status_money == 'insufficient_funds':
                  tomorrow_pay = AutoPayModel(uuid=uuid, email=email_client, amount=amount, \
                                          date_now=date_now, date_next_month=tomorrow)
                  tomorrow_pay.save()
                  send_mail(
                    'Автоплатеж',
                    'На карте не хватает денег для оплаты.\n'
                    'Платеж будет перенесен на завтра, если вы хотите отказаться от ежемесячных платежей перейдите по ссылке для отмены автоплатежа: '
                    f'http://135.181.198.180:25010/transfer-abort/{uuid}/',
                    f'{EMAIL_HOST_USER}',
                   [f'{email_client}'],
                     fail_silently=False,
                      )
              else:
                  uuid = payment.payment_method.id
                  amount = payment.amount.value
                  date_now = payment.created_at
                  date_now = datetime.strptime(date_now, "%Y-%m-%dT%H:%M:%S.%fZ")
                  date_now = date_now.date()
                  date_next_month = date_now + relativedelta(months=1)
                  auto_pay = AutoPayModel(uuid=uuid, email=email_client, amount=amount, \
                                          date_now=date_now, date_next_month=date_next_month)
                  auto_pay.save()
                  send_mail(
                      'Отмена Автоплатежа',
                      f'Для отмены автоплатежа перейдите по ссылке:\n'
                      f'http://135.181.198.180:25010/transfer-abort/{uuid}/',
                      f'{EMAIL_HOST_USER}',
                      [f'{email_client}'],
                      fail_silently=False,
                  )









