from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    name = models.CharField("name", max_length=500)
    surname = models.CharField("surname", max_length=500)
    invite_code = models.CharField("invite code", max_length=11, null=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.invite_code}"
