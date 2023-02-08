from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

# parent
router.register(prefix='booking',
                viewset=views.BookedDonationViewSet,
                basename='booked-donation'
                )

urlpatterns = router.urls
