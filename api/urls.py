from django.urls import path
from .views import SmallestViewSet,StatsViewSet

urlpatterns = [
    path('smallest', SmallestViewSet.as_view(), name='smallest'),
    path('stats', StatsViewSet.as_view(), name='stats')
]