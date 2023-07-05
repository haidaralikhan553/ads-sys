from django.db import models
from authentication.models import CustomUser

class Ads(models.Model):
    ad_name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.ad_name

    def save(self, *args, **kwargs):
        is_new_ad = not self.pk
        super().save(*args, **kwargs)
        if is_new_ad:
            AdviewCounter.objects.create(ad=self, count=0, max_count=200, location="khi")
            AdviewCounter.objects.create(ad=self, count=0, max_count=1000, location="mul")
            AdviewCounter.objects.create(ad=self, count=0, max_count=100, location="lhr")


class AdviewCounter(models.Model):
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, null=True, blank=True)
    max_count = models.IntegerField(default=1000, null=True, blank=True)
    location = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.ad.ad_name + " : " + str(self.count)
