from celery import shared_task
from celery.signals import task_success, task_failure
from django.core.management import call_command
from django.core.mail import send_mail
from core.settings_ import settings
EMAIL_HOST_USER = settings.EMAIL_HOST_USER.get_secret_value()
EMAIL_REPORT = settings.EMAIL_REPORT.get_secret_value()


@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 4, 'countdown': 7200})
def auto_pay(self):
    try:
        call_command('auto', )
    except  Exception:
        raise Exception()

@task_success.connect(sender=auto_pay)
def task_success_notifier(sender=None, **kwargs):
   print('Задание выполнено успешно!')

@task_failure.connect(sender=auto_pay)
def task_failure_notifier(sender=None, **kwargs):
   print('ПРОИЗОШЕЛ СБОЙ ЗАДАНИЯ!!!')
   send_mail(
       'Ошибка',
       'Ошибка в задании автоплатежей',
       f'{EMAIL_HOST_USER}',
       [f'{EMAIL_REPORT}'],
        fail_silently=False,
   )



