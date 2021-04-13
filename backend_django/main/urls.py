
from django.urls import path
from .views.auth import login, test_api_unrestricted
from .views.auth_sso import login_with_sso

from .views.views_peminjaman_ruangan import update_peminjaman_ruangan_by_id_peminjaman_ruangan, get_post_peminjaman_ruangan_unit_kerja

urlpatterns = [
    path('login/', login),
    path('test-api/', test_api_unrestricted),
    path('login-sso/', login_with_sso),
    path('peminjaman-ruangan/update/<int:id_peminjaman>/', update_peminjaman_ruangan_by_id_peminjaman_ruangan),
    path('peminjaman-ruangan/unit-kerja/', get_post_peminjaman_ruangan_unit_kerja)
]
