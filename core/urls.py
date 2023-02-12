from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
