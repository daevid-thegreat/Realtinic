from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    location = models.CharField(max_length=120, blank=True)


    def __str__(self):
        return self.user.full_name