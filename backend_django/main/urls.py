
# from django.urls import path
# from .views.auth import login, test_api_unrestricted
# from .views.auth_sso import login_with_sso

# from .views.views_peminjaman_ruangan import list_peminjaman_ruangan, post_peminjaman_ruangan_mahasiswa

# from .views.views_humas import 

# urlpatterns = [
#     path('login/', login),
#     path('test-api/', test_api_unrestricted),
#     path('login-sso/', login_with_sso),
#     path('list-peminjaman-ruangan/', list_peminjaman_ruangan ),
#     path('list-perizinan-humas/<pk>', detail_perizinan_humas),
#     path('list-perizinan-humas/',list_perizinan_humas),
#     path('peminjaman-ruangan/mahasiswa/', post_peminjaman_ruangan_mahasiswa) 

# ]
from django.urls import path
from .views.auth import login, test_api_unrestricted
from .views.auth_sso import login_with_sso

from .views.views_peminjaman_ruangan import update_peminjaman_ruangan_by_id_peminjaman_ruangan, get_post_peminjaman_ruangan_unit_kerja, post_peminjaman_ruangan_mahasiswa
from .views.views_humas import get_post_perizinan_humas,list_perizinan_humas
from .views.views_izin_kegiatan_mahasiswa import get_post_izin_kegiatan_mahasiswa

urlpatterns = [
    path('login/', login),
    path('test-api/', test_api_unrestricted),
    path('login-sso/', login_with_sso),
    path('peminjaman-ruangan/update/<int:id_peminjaman>/', update_peminjaman_ruangan_by_id_peminjaman_ruangan),
    path('peminjaman-ruangan/unit-kerja/', get_post_peminjaman_ruangan_unit_kerja),
    path('peminjaman-ruangan/mahasiswa/<int:id_izin_kegiatan>', post_peminjaman_ruangan_mahasiswa),
    path('perizinan-humas/<int:id_izin_kegiatan>',get_post_perizinan_humas),
    path('list-perizinan-humas/',list_perizinan_humas),
    path('perizinan-kegiatan-mahasiswa/',get_post_izin_kegiatan_mahasiswa),
]
