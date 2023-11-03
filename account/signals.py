from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile

def create_profile(sender, instance, created, **kwargs):
    """
    Handles new user by adding them to group Customers and create new Profile.
    """
    if created:
        # Add user to customers group
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        # Create Profile model for user
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)

def update_profile(sender, instance, created, **kwargs):
    """
    Handles existing users and updates their user details.
    """
    if created == False:
        instance.profile.save()

post_save.connect(update_profile, sender=User)