# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
#
# class User(AbstractUser):
#     email = models.EmailField(_("email address"), unique=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
#
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.username

# Profile/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    # Custom fields for Profile.User
    # ...

    groups = models.ManyToManyField(
        Group,
        related_name='profile_user_set',  # Custom related name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='profile_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='profile_user_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='profile_user',
    )
