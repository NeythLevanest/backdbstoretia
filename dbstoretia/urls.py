
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from rest_framework.routers import DefaultRouter

import appstoretia
import appstoretia.views as views
from appstoretia.urls import router

from dbstoretia import settings


from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appstoretia.urls')),
    path('', include(router.urls)),
    path('correlacion_ventas/', views.Correlacion_Ventas.as_view(), name='api_correlacion_ventas'),
    path('promedio_ventas_tienda/', views.Promedio_Ventas.as_view(), name='api_promedio_ventas'),
    path('promedio_global_ventas_tienda/', views.Promedio_Global_Ventas.as_view(), name='api_promediog_ventas'),

]
