from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ObtainTokenPairView, Logout

app_name = 'authentication'

urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', Logout.as_view(), name='logout'),
]
