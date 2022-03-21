"""
AbstractBaseUser - это стратегия использования совершенно новой модели пользователя.
Она подходит нам тогда, когда мы не хотим использовать стандартную аутентификацию
- это то, что нам нужно в нашем конкретном случае.
"""

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from user_registrations.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=30, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    invite_code = models.CharField("invite code", max_length=11, null=True)

    is_verified = models.BooleanField(_('verified'), default=False)
    # нужно для того, чтобы каким-то образом реализовать подтверждение по номеру телефона
    # если код совпадет, то поставим is_verified пользователю

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # логиниться будем по username
    REQUIRED_FIELDS = ['phone']
    # это настройка для джосера

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'phone')
        # позволяет нас создать некий составной ключ из комбинации полей 'username', 'email', 'phone'
        # чтобы пользователи не дублировались
