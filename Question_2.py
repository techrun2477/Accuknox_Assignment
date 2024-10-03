# Question 2: Do Django signals run in the same thread as the caller?

# Yes, by default Django signals run in the same thread as the caller. This means that when the signal is sent, the signal handler is executed in the same thread and will block the main thread until it is completed.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(pre_save, sender=MyModel)
def pre_save_handler(sender, instance, **kwargs):
    print(f"Pre-save signal received for {instance}")
