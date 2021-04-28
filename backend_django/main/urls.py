
from django.urls import path
from .views.auth import login, test_api_unrestricted
from .views.auth_sso import login_with_sso

from .views.views_peminjaman_ruangan import list_peminjaman_ruangan
from .views.views_izin_kegiatan import list_izin_kegiatan, update_izin_kegiatan_by_id_perizinan

from .views.views_peminjaman_ruangan import list_jadwal
from .views.views_ruangan import list_ruangan
from .views.views_peminjaman_ruangan import list_ruangan
from .views.views_peminjaman_ruangan import detail_ruangan
from .views.views_status_perizinan import list_perizinan, detail_perizinan
from .views.views_peminjaman_ruangan import update_peminjaman_ruangan_by_id_peminjaman_ruangan, post_peminjaman_ruangan_unit_kerja, get_list_perizinan_fastur, get_peminjaman_ruangan_by_id_izin_kegiatan

urlpatterns = [
    path('login/', login),
    path('test-api/', test_api_unrestricted),
    path('login-sso/', login_with_sso),
    path('list-peminjaman-ruangan/', list_peminjaman_ruangan),
    path('izin-kegiatan/update/<int:id_perizinan>/', update_izin_kegiatan_by_id_perizinan),
    path('izin-kegiatan/', list_izin_kegiatan),
    path('jadwal-tersedia/', list_jadwal),
    path('api/ruangan/', list_ruangan),
    path('api/ruangan/<int:pk>/', detail_ruangan),
    path('api/list-perizinan/', list_perizinan),
    path('api/perizinan/<int:pk>', detail_perizinan),
    path('peminjaman-ruangan/update-status/<int:id_peminjaman>/', update_peminjaman_ruangan_by_id_peminjaman_ruangan),
    path('peminjaman-ruangan/unit-kerja/', post_peminjaman_ruangan_unit_kerja),
    path('peminjaman-ruangan/verifikasi-fastur/', get_list_perizinan_fastur),
    path('peminjaman-ruangan/verifikasi-fastur/<int:id_izin_kegiatan>/', get_peminjaman_ruangan_by_id_izin_kegiatan),
    
]
