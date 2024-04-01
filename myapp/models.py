from django.db import models
from django.contrib.auth.models import User

class InputNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.user.username}: {self.number}'

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_time} to {self.logout_time}"

    class Meta:
        app_label = 'myapp'
        