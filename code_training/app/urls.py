from rest_framework import routers
from .views import DecisionViewSet


router = routers.DefaultRouter()
router.register(r'decisions', DecisionViewSet)

urlpatterns = router.urls