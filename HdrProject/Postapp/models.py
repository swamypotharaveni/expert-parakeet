from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from django.apps import apps
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, upload_to='media', default='avatar.jpg')
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.email=self.email  # Set username to email by default
        super().save(*args, **kwargs)



    def image_tag(self):
        return mark_safe('<img src="/images/%s" width="100" height="100" border-radius="30">' % (self.avatar))

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'
