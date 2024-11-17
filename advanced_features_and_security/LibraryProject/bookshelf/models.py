from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username


class CustomUser(AbstractUser):
    # Add related_name to groups and user_permissions to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # custom related name for the groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # custom related name for the user_permissions
        blank=True,
    )
