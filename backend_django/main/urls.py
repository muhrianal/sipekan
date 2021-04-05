
from django.urls import path
from .views.auth import login, test_api_unrestricted
from .views.auth_sso import login_with_sso
urlpatterns = [
    path('login/', login),
    path('test-api/', test_api_unrestricted),
    path('login-sso/', login_with_sso)

]
