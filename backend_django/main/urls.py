
from django.urls import path
from .views.auth import login, test_api_unrestricted
from .views.auth_sso import login_with_sso

from .views.views_peminjaman_ruangan import list_peminjaman_ruangan, list_peminjaman_ruangan_by_id_kegiatan, update_peminjaman_ruangan_by_id_peminjaman_ruangan, create_peminjaman_ruangan_unit_kerja

urlpatterns = [
    path('login/', login),
    path('test-api/', test_api_unrestricted),
    path('login-sso/', login_with_sso),
    path('list-peminjaman-ruangan/', list_peminjaman_ruangan),
    path('peminjaman-ruangan/get-by-id-kegiatan/<int:id_kegiatan>/', list_peminjaman_ruangan_by_id_kegiatan),
    path('peminjaman-ruangan/update/<int:id_peminjaman>/', update_peminjaman_ruangan_by_id_peminjaman_ruangan),
    path('peminjaman-ruangan/unit-kerja/create/', create_peminjaman_ruangan_unit_kerja)
]
