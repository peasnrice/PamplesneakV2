from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    def __unicode__(self):
        return self.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])