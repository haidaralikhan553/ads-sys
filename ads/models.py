from django.db import models
from authentication.models import CustomUser

class Ads(models.Model):
    ad_name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        is_new_ad = not self.pk
        super().save(*args, **kwargs)
        if is_new_ad:
            UserProfile.objects.create(ad=self)


class AdviewCounter(models.Model):
    ad = models.ForeignKey(Ads, ondelete=models.CASCADE)
    count = models.IntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=20, blank=True, null=True)
