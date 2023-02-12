from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('email', views.EmailViewSet, 'email')
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
