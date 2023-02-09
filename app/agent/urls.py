from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

# parent
router.register(prefix='booking',
                viewset=views.BookedDonationViewSet,
                basename='booking'
                )
# FIXME :temp
router.register(prefix='orders',
                viewset=views.OrderViewSet,
                basename='orders'
                )

urlpatterns = router.urls
