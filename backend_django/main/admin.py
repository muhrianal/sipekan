from django.contrib import admin

from .models.profile import Profile
from .models.izin_kegiatan import IzinKegiatan, DetailKegiatan

# Register your models here.
admin.site.register(Profile)

admin.site.register(IzinKegiatan)

admin.site.register(DetailKegiatan)

