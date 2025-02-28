from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True )
    
    class Meta:
        permissions = [
            ("can_add_book","Can add book"),
            ("can_delete_book", "Can delete book"),
            ("can_change_book", "Can change book"),
        ]
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# That I added models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    role_choice = (
         ("Admin", 'Admin'),
        ("Librarian", "Librarian"),
        ("Member",  "Member"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=role_choice)

    def __str__(self):
        return self.user.username
    

# Siginal to create or update Userprofile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
"""
class UserProfile(models.Model):
    USER_ROLES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="userprofile"
    )
    role = models.CharField(max_length=255, choices=USER_ROLES)

    def __str__(self):
        return self.user.username + " " + self.role

    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_profile, sender=User)

    def update_profile(sender, instance, created, **kwargs):
        if created is False:
            instance.userprofile.save()

    post_save.connect(update_profile, sender=User)"""