from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_phonebook-api'

router = NetBoxRouter()
router.register('number', views.NumberViewSet, basename='number')

urlpatterns = router.urls
