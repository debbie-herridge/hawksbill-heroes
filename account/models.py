from django.db import models
from django.contrib.auth.models import User

# User profile model
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile-picture")

    def __str__(self):
        return str(self.user)

        