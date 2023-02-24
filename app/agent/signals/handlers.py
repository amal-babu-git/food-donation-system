from django.db.models.signals import post_save
from django.db import transaction
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from agent.models import Order
from agent.serializers import OrderSerializer


# send mail to donar , after booking of donation


@receiver(post_save, sender=Order)
def send_mail_to_donar(sender, **kwargs):
    subject = 'Your Donation successfully booked by an agent'
    message = 'Hi, Your order successfully booked.\n'

    if kwargs['created']:

        with transaction.atomic():
            # details=[{key,value} for key ,value in kwargs['instance'] ]
            # print('signal test ', kwargs['instance'])
            serializer = OrderSerializer(kwargs['instance'])
            # print('data', serializer.data)
            agent_email = serializer.data['user']
            # donar details includes user(email),address FIXME: fix this complex process in future,add an email field in donar modal and order modal
            donar_details = serializer.data['donar_details']
            # extracting email
            donar_email = [str(i) for i in str(donar_details).split(',')][0]
            # print(donar_email)

            message += 'Agent contact: '+agent_email + \
                "\n Details: "+str(serializer.data)
            try:
                send_mail(subject=subject, message=message,
                          from_email=settings.DEFAULT_FROM_EMAIL,
                          recipient_list=[f'{donar_email}',])

            except Exception as e:
                print(e)


# send_mail_to_donar()
