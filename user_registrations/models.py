from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from user_registrations.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""
    username = models.CharField(_('username'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=30, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    invite_code = models.CharField("invite code", max_length=11, null=True)
    entered_invite_code = models.CharField("entered invite code", max_length=11, null=True)
    your_invitees = models.CharField("your invitees", max_length=500, null=True)

    is_verified = models.BooleanField(_('verified'), default=False)
    # нужно для того, чтобы каким-то образом реализовать подтверждение по номеру телефона
    # если код совпадет, то поставим is_verified пользователю

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'invite_code', 'entered_invite_code']  # djoser - доп поля выводить при auth/users/me/

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'phone')
