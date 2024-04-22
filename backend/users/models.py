from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, first_name, password, last_name = ""):
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, password, last_name = ""):

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    def __str__(self):
        return self.first_name
    
    