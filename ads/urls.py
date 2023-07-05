from django.urls import path, include
from rest_framework import routers

from .views import AdsViewSet

app_name = 'contacted'

router = routers.DefaultRouter()
router.register("", AdsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
