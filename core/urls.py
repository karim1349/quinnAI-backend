from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.urls import router
from users.views import get_token

urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('admin/', admin.site.urls),
    path("oauth/", include("allauth.urls")),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/token/get_token/', get_token, name='get_verify'),

]
