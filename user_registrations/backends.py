from user_registrations.models import User
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class AuthBackend(object):
    supports_object_permissions = True  # поддержка пермишенов на уровне объекта модели
    supports_anonymous_user = False  # выключение поддержки анонимных пользователей, чтобы не логинились
    supports_inactive_user = False  # выключение поддержки неактивных пользователей

    def get_user(self, user_id):
        """служебный метод, без которого не можем обойтись"""
        try:
           return User.objects.get(pk=user_id)
        except User.DoesNotExist:
           return None

    def authenticate(self, request, username, password):
        """Получает пользователя по одному из трёх полей"""

        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )

        except User.DoesNotExist:
            return None

        if user.check_password(password):
            """Правильно ли пользователь пароль ввёл"""
            return user

        else:
            return None
