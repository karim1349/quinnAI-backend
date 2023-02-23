from django.contrib import admin
from django.urls import include, path
from api import views
from api.urls import router

urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('admin/', admin.site.urls),
]
