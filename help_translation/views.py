import time
import datetime
import uuid as myuuid
from rest_framework import status
from rest_framework import request
from django.core.mail import send_mail
from yookassa import Configuration, Payment
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta
from core.settings import account_id, secret_key
from rest_framework.viewsets import ModelViewSet
from core.settings import EMAIL_HOST_USER
from help_translation.models import HelpTranlationModel, AutoPayModel
from help_translation.serializers import HelpTranlationSerializer, AutoPaySerializer


Configuration.account_id = account_id
Configuration.secret_key = secret_key

__all__ = (
    'HelpTranlationView',
    'AutoPayView',
)


class AutoPayView(ModelViewSet):
    queryset = AutoPayModel.objects.all()
    serializer_class = AutoPaySerializer
    http_method_names = ['delete']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class HelpTranlationView(ModelViewSet):
    queryset = HelpTranlationModel.objects.all()
    serializer_class = HelpTranlationSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         if serializer.data['one_time'] == True:
          if serializer.data['type_transfer'] == "bank_card":
            amount = serializer.data['amount']
            comment = serializer.data['comment']
            phone =  serializer.data['phone']
            idempotence_key = str(myuuid.uuid4())
            payment = Payment.create({
                 "amount": {
                    "value": f"{amount}.00",
                    "currency": "RUB"
                 },
                 "payment_method_data": {
                    "type": "bank_card"
                 },
                 "confirmation": {
                     "type": "redirect",
                     "return_url": "http://135.181.198.180:25010/transfer-success"
                 },
                 "description": f"{comment}"
             }, idempotence_key)
            confirmation_url = payment.confirmation.confirmation_url
            return Response({"href": f"{confirmation_url}"})
          elif serializer.data['type_transfer'] == "mobile_balance":
                idempotence_key = str(myuuid.uuid4())
                payment = Payment.create({
                    "amount": {
                        "value": f"{amount}.00",
                        "currency": "RUB"
                    },
                    "payment_method_data": {
                        "type": "mobile_balance",
                        "phone": f"{phone}"
                    },
                    "confirmation": {
                        "type": "external"
                    },
                    "description": f"{comment}"
                }, idempotence_key)
                confirmation_url = payment.confirmation.confirmation_url
                return Response({"href": f"{confirmation_url}"})
          elif serializer.data['type_transfer'] == "sbp":
                idempotence_key = str(myuuid.uuid4())
                payment = Payment.create({
                    "amount": {
                        "value": f"{amount}.00",
                        "currency": "RUB"
                    },
                    "payment_method_data": {
                        "type": "sbp"
                    },
                    "confirmation": {
                        "type": "redirect",
                        "return_url": "http://135.181.198.180:25010/transfer-success"
                    },
                    "description": f"{comment}"
                }, idempotence_key)

                confirmation_url = payment.confirmation.confirmation_url
                return Response({"href": f"{confirmation_url}"})
          else:
                return Response({"error": "400"})
         elif serializer.data['monthly'] == True:
          amount = serializer.data['amount']
          comment = serializer.data['comment']
          phone = serializer.data['phone']
          email = serializer.data['email']
          if serializer.data['type_transfer'] == "bank_card":
              idempotence_key = str(myuuid.uuid4())
              payment = Payment.create({
                  "amount": {
                      "value": f"{amount}.00",
                      "currency": "RUB"
                  },
                  "payment_method_data": {
                      "type": "bank_card"
                  },
                  "confirmation": {
                      "type": "redirect",
                      "return_url": "http://135.181.198.180:25010/transfer-success"
                  },
                  "capture": True,
                  "description": f"{comment}",
                  "save_payment_method": True
              }, idempotence_key)
              confirmation_url = payment.confirmation.confirmation_url
              uuid = payment.payment_method.id
              amount = payment.amount.value
              saved = payment.payment_method.saved
              cr_date = payment.created_at
              cr_date = datetime.datetime.strptime(cr_date, "%Y-%m-%dT%H:%M:%S.%fZ")
              cr_date = cr_date.date()
              date_next_month = cr_date + relativedelta(months=1)
              status = payment.status
              auto_pay = AutoPayModel(uuid=uuid, email=email,amount=amount, \
                                          date_now=cr_date, date_next_month=date_next_month)
              auto_pay.save()
              send_mail(
                  'Отмена Автоплатежа',
                  f'Для отмены Автоплатежа перейдите по ссылке:\n'
                  f'http://135.181.198.180:25010/transfer-abort/{uuid}/',
                  f'{EMAIL_HOST_USER}',
                  [f'{email}'],
                  fail_silently=False,
              )
              return Response({"href": f"{confirmation_url}"})
          elif serializer.data['type_transfer'] == "sbp":
              idempotence_key = str(myuuid.uuid4())
              payment = Payment.create({
                  "amount": {
                      "value": f"{amount}.00",
                      "currency": "RUB"
                  },
                  "payment_method_data": {
                      "type": "sbp"
                  },
                  "confirmation": {
                      "type": "redirect",
                      "return_url": "http://135.181.198.180:25010/transfer-success"
                  },
                  "capture": True,
                  "description": f"{comment}",
                  "save_payment_method": True
              }, idempotence_key)
              confirmation_url = payment.confirmation.confirmation_url
              uuid = payment.payment_method.id
              amount = payment.amount.value
              saved = payment.payment_method.saved
              cr_date = payment.created_at
              cr_date = datetime.datetime.strptime(cr_date, "%Y-%m-%dT%H:%M:%S.%fZ")
              cr_date = cr_date.date()
              date_next_month = cr_date + relativedelta(months=1)
              status = payment.status
              auto_pay = AutoPayModel(uuid=uuid, email=email, amount=amount, \
                                      date_now=cr_date, date_next_month=date_next_month)
              auto_pay.save()
              send_mail(
                  'Отмена Автоплатежа',
                  f'Для отмены Автоплатежа перейдите по ссылке:\n'
                  f'http://135.181.198.180:25010/transfer-abort/{uuid}/',

                  f'{EMAIL_HOST_USER}',
                  [f'{email}'],
                  fail_silently=False,
              )
              return Response({"href": f"{confirmation_url}"})
          else:
              return Response({"error": "400"})






