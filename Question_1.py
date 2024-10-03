# Question 1: By default are Django signals executed synchronously or asynchronously?

# Answer: Django signals are executed synchronously by default. This means that the signal handlers (the functions connected to the signals) are executed in the same thread and in the same request/response cycle that triggered the signal.

# You can execute signals asynchronously by using Django's asynchronous features or by running the signal handlers in a separate thread or background job queue (like Celery).
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance} has been created!")
