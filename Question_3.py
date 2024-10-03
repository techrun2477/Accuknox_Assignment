# Question 3: By default, do Django signals run in the same database transaction as the caller?

# Answer: Yes, Django signals, such as post_save and post_delete, are fired after the database transaction is committed. However, pre_save and pre_delete signals are fired before the transaction is completed.

#To ensure that signals are run in the same transaction, you can use Django’s transaction.on_commit() method, which executes a callback only after the transaction is successfully committed.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def post_save_handler(sender, instance, **kwargs):
    transaction.on_commit(lambda: print(f"Transaction committed for {instance}"))
