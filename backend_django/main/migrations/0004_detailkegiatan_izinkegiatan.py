# Generated by Django 3.1.7 on 2021-04-05 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210405_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='IzinKegiatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kegiatan', models.CharField(max_length=255)),
                ('organisasi', models.CharField(max_length=255)),
                ('status_perizinan_kegiatan', models.PositiveSmallIntegerField(choices=[(1, 'Menunggu Persetujuan'), (2, 'Disetujui'), (3, 'Ditolak')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetailKegiatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_tangal_mulai', models.DateTimeField()),
                ('waktu_tangal_akhir', models.DateTimeField()),
                ('email_pic', models.EmailField(max_length=254)),
                ('nama_pic', models.CharField(max_length=255)),
                ('hp_pic', models.CharField(max_length=255)),
                ('npm_ketua_organisasi', models.CharField(max_length=255)),
                ('nama_ketua_organisasi', models.CharField(max_length=255)),
                ('tempat_pelaksanaan', models.CharField(max_length=255)),
                ('sumber_pendanaan', models.CharField(max_length=255)),
                ('alasan_penolakan', models.CharField(max_length=500)),
                ('file_info_kegiatan', models.FileField(upload_to='file_kegiatan')),
                ('izin_kegiatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.izinkegiatan')),
            ],
        ),
    ]
