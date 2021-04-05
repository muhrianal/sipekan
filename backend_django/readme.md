
# Backend SIPEKAN w/ **Django**


## Persiapan

1. Clone Repository ini dengan:

```
git clone https://github.com/muhrianal/sipekan.git
```

2. Install dan buat virtual environment python (kalau lupa bisa cari di Internet, disini tidak dicantumkan karena tiap OS beda caranya)
3. Jangan lupa aktifkan virtual environment-nya
4. Install dependencies-nya

```
pip install -r requirements.txt
```

4. Django app sudah bisa dijalankan

Sebelumnya, jalankan dulu perintah berintah berikut:
```
python manage.py makemigrations
python manage.py migrate
```

perintah di atas harus dijalankan setiap terjadi perubahan di model, admin, dll

untuk menjalankan aplikasi
```
python manage.py runserver
```

## Tentang GIT

* Buat terlebih dahulu branch masing-masing
```
git branch dev/{nama_kalian}
```

Setelah menjalankan perintah diatas, kamu baru membuat branch namun belum berpindah ke branch tersebut

* Pindah ke branch yang telah kalian buat
```
git checkout dev/{nama_kalian}
```

Cara lain untuk membuat branch sekaligus langsung berpindah ke branch tersebut:
```
git checkout -b dev/{nama_kalian}
```

#### Untuk ngepush:

* Cek dulu udah di branch masing-masing atau belum 
```
git status
```

Kalo branch-nya masih belum di branch masing-masing, pindah dulu yaaa pake cara sebelumnya.

Kalo udh di branch:
```
git add .
git commit -m "jelasin disini tujuan ngepushnya apa (misal apa yang diubah)"
git push origin dev/{nama_kalian}
```

Perhatikan bahwa saat jalanin git add itu diakhiri dengan titik yang artinya ngepush semua yang telah diubah. Kalo misal mau ngepush salah satu file doang bisa diganti jadi:
```
git add directory/to/the/file
```

##


link referensi API : https://bezkoder.com/django-rest-api/