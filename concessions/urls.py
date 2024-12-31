from rest_framework_nested import routers
from .views import ConcessionViewSet, VehiculeViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'concessions', ConcessionViewSet)

concession_router = routers.NestedSimpleRouter(router, r'concessions', lookup='concession')
concession_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(concession_router.urls)),
]
