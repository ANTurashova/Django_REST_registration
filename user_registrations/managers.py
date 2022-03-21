from django.contrib.auth.base_user import BaseUserManager
from random import sample
from string import ascii_lowercase, digits


def generate_invite_code():
    return ''.join(sample(ascii_lowercase + digits, 10))


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username=None, phone=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        Принимает в себя данные по пользователю, доп поля.
        В методе реализовано несколько проверочек.
        """

        if not username:
            username = phone

        invite_code = generate_invite_code()

        user = self.model(
            username=username,
            phone=phone,
            invite_code=invite_code,
            **extra_fields
        )
        
        # проверяем является ли пользователь
        # суперпользователем
        if extra_fields.get('is_superuser'):
            user = self.model(
                username=username,
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone, password=None, **extra_fields):
        """метод для создания пользователя"""
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, phone=phone, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """метод для создания суперпользователя"""
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            # если нам приходит is_superuser = False в методе create_superuser, кидаем ошибку
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(
            username=username,
            password=password,
            **extra_fields
        )
