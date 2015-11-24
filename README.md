Media Komunitas 160 Karakter
============================
Merupakan media komunitas berbasis SMS. Penggunaan media ini cocok untuk wilayah-wilayah Indonesia yang masih belum terjamah koneksi internet. Pemanfaatannya bisa dari penyebaran berita hingga advokasi.

Requirement:
============
* Django==1.8.6
* MySQL-python==1.2.5
* PyYAML==3.11
* SQLAlchemy==0.8.0b2
* appnope==0.1.0
* decorator==4.0.4
* django-autocomplete-light==2.2.10
* django-chosen==0.1
* django-filter==0.11.0
* django-grappelli==2.7.2
* django-remote-forms==0.0.1
* django-rest-swagger==0.3.4
* django-smart-selects==1.1.1
* djangorestframework==3.3.1
* gnureadline==6.3.3
* ipython==4.0.0
* ipython-genutils==0.1.0
* path.py==8.1.2
* pexpect==4.0.1
* pickleshare==0.5
* ptyprocess==0.5
* simplegeneric==0.8.1
* six==1.10.0
* traitlets==4.0.0
* wsgiref==0.1.2



Changelog :
===========
* 24 November 2015
  - Menambahkan API untuk member family, person dan message
  - Menyertakan file virtualenv
  - Mengubah tampilan halaman admin
  - Menambahkan API untuk importing data awal (json)
  - Menambahkan fixture untuk data statis

* 17 Oktober 2014
  - Menambahkan halaman statistik 
  - Menampilkan kata paling sering dipakai dalam sms. Dalam bentuk word cloud

* 17 April 2013
	- Menambahkan database non member
	- Menambahkan field member yang ulang tahun
	
* 20 Maret 2013
  - Menggunakan Chained ForeignKey field untuk address
  - Memperbaiki form organisasi
  - Penambahan search fields
  
* 20 Oktober 2012
  - Perbaiki masking untuk menampilkan teks kosong
  - Perbaikan pengiriman sms, memeriksa field kosong

* 19 Oktober 2012
  - Upgrade skema project menganut Django 1.4
  - Tambah aplikasi Account
  - Tambah fitur Reply SMS

LISENSI
=======
Karena dari awal pengembangannya sudah memakai lisensi GPL, maka ya apa boleh bikin..
