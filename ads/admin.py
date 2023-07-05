from django.contrib import admin

# Register your models here.
from .models import Ads, AdviewCounter

admin.site.register(Ads)
admin.site.register(AdviewCounter)
