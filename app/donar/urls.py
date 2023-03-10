from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

# parent
router.register(prefix='',
                viewset=views.DonationViewSet,
                basename='donation'
                )

urlpatterns = router.urls
