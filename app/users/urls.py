from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

# parent
router.register(prefix='',
                viewset=views.UserViewSet,
                basename='user'
                )

urlpatterns = router.urls
