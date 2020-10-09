from rest_framework.urlpatterns import format_suffix_patterns

from appstoretia import views

from appstoretia.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'ventas', VentasViewSet)
router.register(r'caracteristicas', CaracteristicasViewSet)
router.register(r'tiendas', TiendasViewSet)



urlpatterns = router.urls