from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response 

from .models import Ads, AdviewCounter
from .serializers import AdsSerializer
from .permissions import CanAccessAds
        

class AdsViewSet(viewsets.ModelViewSet):
    """ViewSet for the contacted class"""

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [CanAccessAds]
    # pagination

    @action(detail=False, methods=['get'])
    def resetall(self, request):
        if not request.user.is_superuser:
            return Response({'error': 'Only super admin can update the status field.'}, status=403)
        
        all_adview_counters = AdviewCounter.objects.all()
        for adview_counter in all_adview_counters:
            adview_counter.count = 0
            adview_counter.save()

        return Response(data={'message': 'Ad views reset done'}, status=status.HTTP_205_RESET_CONTENT)

    @action(detail=True, methods=['get'])
    def reset(self, request, pk=None):
        location = request.GET.get('location', 'abcd')
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if not request.user.is_superuser:
            return Response({'error': 'Only super admin can update the status field.'}, status=403)
        
        try:
            adview_counter = AdviewCounter.objects.filter(ad=instance, location=location.lower()).first()
            adview_counter.count = 0
            adview_counter.save()
        except AdviewCounter.DoesNotExist:
            AdviewCounter.objects.create(ad=instance, count=0)
        except Exception as e:
            pass

        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, *args, **kwargs):
        location = request.GET.get('location', 'abcd')
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        try:
            adview_counter = AdviewCounter.objects.filter(ad=instance, location=location.lower()).first()
            if adview_counter.count >= adview_counter.max_count:
                return Response(data={'message': 'No content found'}, status=status.HTTP_404_NOT_FOUND)
            adview_counter.count += 1
            adview_counter.save()
        except AdviewCounter.DoesNotExist:
            AdviewCounter.objects.create(ad=instance, count=0)
        except Exception as e:
            pass

        return Response(serializer.data, status=status.HTTP_200_OK)