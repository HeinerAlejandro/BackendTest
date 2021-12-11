from rest_framework.routers import DefaultRouter

from .views import PollAPIView

router = DefaultRouter()

router.register(r'polls', PollAPIView, basename='polls')

urlpatterns = router.urls
