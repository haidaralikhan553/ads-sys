from rest_framework import viewsets

from .models import Ads
from .serializers import AdsSerializer
from .permissions import CanAccessAds


class AdsViewSet(viewsets.ModelViewSet):
    """ViewSet for the contacted class"""

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [CanAccessAds]
    # pagination

    def retrieve(self, request, *args, **kwargs):
        location = request.GET.get('location', None)
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        try:
            adview_counter = AdviewCounter.objects.get(ad=instance, location=location)
            adview_counter.count += 1
            adview_counter.save()
        except AdviewCounter.DoesNotExist:
            AdviewCounter.objects.create(ad=instance, count=1)

        return Response(serializer.data, status=status.HTTP_200_OK)