from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'departements', views.DepartementsViewSet)
router.register(r'provinces', views.ProvincesViewSet)
router.register(r'Regions', views.RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]