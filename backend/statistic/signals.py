from django.db.models.signals import post_save
from .models import (
    model_action_choices,
    Log,
    BigLottery
)


def saveLog(sender, instance, created, **kwargs):
    action = model_action_choices[1][0] if created else model_action_choices[2][0]
    Log.objects.create(model=sender, instance=instance, action=action)

post_save.connect(saveLog, sender=BigLottery)