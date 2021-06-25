from rest_framework import routers, urlpatterns
from .views import EvaluationViewSet

router=routers.DefaultRouter()
router.register('evaluation',EvaluationViewSet)
urlpatterns=  router.urls