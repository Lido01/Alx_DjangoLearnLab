#class CustomBackend(BaseBackend):
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


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
    mobile = models.CharField(max_length=15, unique=True)
    
    #objects = CustomUserManager()
    USERNAME_FIELD = "email" #assign unique that user must get to login
    REQUIRED_FIELDS = ["username"]
