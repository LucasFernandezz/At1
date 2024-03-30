# signals.py
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth import logout

@receiver(request_finished)
def handle_request_finished(sender, **kwargs):
    # Perform logout when server connection is closed
    logout()
