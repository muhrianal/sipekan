
from django.urls import path
from .views.auth import login, test_api_unrestricted
from .views.auth_sso import login_with_sso

from .views.views_peminjaman_ruangan import list_peminjaman_ruangan
from .views.views_peminjaman_ruangan import list_ruangan
from .views.views_peminjaman_ruangan import detail_ruangan
from .views.views_status_perizinan import list_perizinan, detail_perizinan

urlpatterns = [
    path('login/', login),
    path('test-api/', test_api_unrestricted),
    path('login-sso/', login_with_sso),
    path('list-peminjaman-ruangan/', list_peminjaman_ruangan),
    path('api/ruangan/', list_ruangan),
    path('api/ruangan/<int:pk>/', detail_ruangan),
    path('api/list-perizinan/', list_perizinan),
    path('api/perizinan/<int:pk>', detail_perizinan)
]
