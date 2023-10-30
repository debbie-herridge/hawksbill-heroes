from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile

def create_profile(sender, instance, created, **kwargs):

    if created:
        # add user to customers group
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        # create Profile model for user
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()

post_save.connect(update_profile, sender=User)