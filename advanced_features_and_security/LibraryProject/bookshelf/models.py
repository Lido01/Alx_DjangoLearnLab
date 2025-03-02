from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.backends import BaseBackend

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


    class Meta:
        permissions = [
            ("can_create_book", "Can create book"),
            ("can_delete_book", "Can delete book"),
            ("can_view_book", "Can view book"),
            ("can_change_book", "Can change book"),
        ]

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField(null=True, blank=True) 
    profile_photo = models.ImageField(null=True, blank=True) #upload_to='profile_photos/', 
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set',blank=True)
    user_permissions = models.ManyToManyField('auth.Permission',related_name='customuser_set',blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email" #assign unique that user must get to login
    REQUIRED_FIELDS = ["username"]
