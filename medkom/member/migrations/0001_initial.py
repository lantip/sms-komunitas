# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('wilayah', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agama',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agama', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Agama',
                'verbose_name_plural': 'Agama',
            },
        ),
        migrations.CreateModel(
            name='AlatTransportasi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alat_transportasi', models.CharField(max_length=50)),
                ('status_social_score', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Alat Transportasi',
                'verbose_name_plural': 'Alat Transportasi',
            },
        ),
        migrations.CreateModel(
            name='Atap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atap', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Kondisi Atap',
                'verbose_name_plural': 'Kondisi Atap',
            },
        ),
        migrations.CreateModel(
            name='DayaListrik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('besar_daya', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Besar Daya Listrik',
                'verbose_name_plural': 'Besar Daya Listrik',
            },
        ),
        migrations.CreateModel(
            name='Dinding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dinding', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Kondisi Dinding',
                'verbose_name_plural': 'Kondisi Dinding',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomor_quesioner', models.CharField(max_length=6)),
                ('nomor_kk', models.CharField(max_length=100)),
                ('penerima_jamsos', models.BooleanField()),
                ('kepemilikan_wc', models.BooleanField()),
                ('alamat_desa', models.ForeignKey(blank=True, to='wilayah.Desa', null=True)),
                ('alamat_dusun', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'nama_desa', chained_field=b'alamat_desa', blank=True, auto_choose=True, to='wilayah.Dusun', null=True)),
                ('alamat_kampung', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'nama_dusun', chained_field=b'alamat_dusun', blank=True, auto_choose=True, to='wilayah.Kampung', null=True)),
                ('alamat_rt', models.ForeignKey(blank=True, to='wilayah.RT', null=True)),
                ('atap', models.ForeignKey(to='member.Atap')),
                ('daya_listrik', models.ForeignKey(blank=True, to='member.DayaListrik', null=True)),
                ('dinding', models.ForeignKey(to='member.Dinding')),
            ],
            options={
                'verbose_name': 'Kartu Keluarga',
                'verbose_name_plural': 'Kartu Keluarga',
            },
        ),
        migrations.CreateModel(
            name='GolonganDarah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('golongan_darah', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Golongan Darah',
                'verbose_name_plural': 'Golongan Darah',
            },
        ),
        migrations.CreateModel(
            name='Handphone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomor_handphone', models.CharField(max_length=15)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Nomor Handphone',
                'verbose_name_plural': 'Nomor Handphone',
            },
        ),
        migrations.CreateModel(
            name='Hobi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hobi', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Hobi',
                'verbose_name_plural': 'Hobi',
            },
        ),
        migrations.CreateModel(
            name='HubunganKeluarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hubungan_keluarga', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Hubungan Keluarga',
                'verbose_name_plural': 'Hubungan Keluarga',
            },
        ),
        migrations.CreateModel(
            name='JadwalRonda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jadwal_ronda', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Jadwal Ronda',
                'verbose_name_plural': 'Jadwal Ronda',
            },
        ),
        migrations.CreateModel(
            name='JamsosDiterima',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jamsos_diterima', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Jamsos Diterima',
                'verbose_name_plural': 'Jamsos Diterima',
            },
        ),
        migrations.CreateModel(
            name='JenisDifable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis_difable', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Jenis Difable',
                'verbose_name_plural': 'Jenis Difable',
            },
        ),
        migrations.CreateModel(
            name='JenisUsaha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis_usaha', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Jenis Usaha',
                'verbose_name_plural': 'Jenis Usaha',
            },
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jurusan', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Jurusan',
                'verbose_name_plural': 'Jurusan',
            },
        ),
        migrations.CreateModel(
            name='Keahlian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keahlian', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Keahlian',
                'verbose_name_plural': 'Keahlian',
            },
        ),
        migrations.CreateModel(
            name='KeluargaGangguan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jumlah_difable', models.IntegerField()),
                ('family', models.ForeignKey(to='member.Family')),
                ('jenis_difable', models.ForeignKey(to='member.JenisDifable')),
            ],
            options={
                'verbose_name': 'Gangguan Fisik',
                'verbose_name_plural': 'Gangguan Fisik',
            },
        ),
        migrations.CreateModel(
            name='Lantai',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lantai', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Kondisi Lantai',
                'verbose_name_plural': 'Kondisi Lantai',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_yang_dipakai', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Organisasi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organisasi', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=50)),
                ('nama_desa', models.ForeignKey(to='wilayah.Desa')),
                ('nama_dusun', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'nama_desa', default=0, blank=True, auto_choose=True, to='wilayah.Dusun', chained_field=b'nama_desa', null=True)),
                ('nama_kampung', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'nama_dusun', default=0, blank=True, auto_choose=True, to='wilayah.Kampung', chained_field=b'nama_dusun', null=True)),
                ('rt', models.ForeignKey(default=0, blank=True, to='wilayah.RT', null=True)),
            ],
            options={
                'verbose_name': 'Organisasi',
                'verbose_name_plural': 'Organisasi',
            },
        ),
        migrations.CreateModel(
            name='Pekerjaan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pekerjaan', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Jenis Pekerjaan',
                'verbose_name_plural': 'Jenis Pekerjaan',
            },
        ),
        migrations.CreateModel(
            name='PendidikanTerakhir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pendidikan_terakhir', models.CharField(max_length=5)),
                ('status_social_score', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Pendidikan Terakhir',
                'verbose_name_plural': 'Pendidikan Terakhir',
            },
        ),
        migrations.CreateModel(
            name='PenghasilanBulanan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nilai_min', models.DecimalField(max_digits=10, decimal_places=2)),
                ('nilai_max', models.DecimalField(max_digits=10, decimal_places=2)),
                ('status_social_score', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Penghasilan Bulanan',
                'verbose_name_plural': 'Penghasilan Bulanan',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('nama_panggilan', models.CharField(max_length=20, blank=True)),
                ('nomor_nik', models.CharField(max_length=30, blank=True)),
                ('tempat_lahir', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.IntegerField(default=0, choices=[(0, b'Laki Laki'), (1, b'Perempuan')])),
                ('status_ktp', models.BooleanField()),
                ('domisili', models.CharField(max_length=50, blank=True)),
                ('tahun_lulus', models.IntegerField(blank=True, null=True, choices=[(1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)])),
                ('no_handphone', models.CharField(max_length=15, blank=True)),
                ('pendonor_darah', models.BooleanField()),
                ('status_social_score', models.PositiveIntegerField(default=0)),
                ('agama', models.ForeignKey(to='member.Agama')),
                ('alat_transportasi', models.ManyToManyField(to='member.AlatTransportasi', blank=True)),
                ('family', models.ForeignKey(to='member.Family')),
                ('golongan_darah', models.ForeignKey(blank=True, to='member.GolonganDarah', null=True)),
                ('hobi', models.ManyToManyField(to='member.Hobi', blank=True)),
                ('hubungan_keluarga', models.ForeignKey(to='member.HubunganKeluarga')),
                ('jenis_usaha', models.ManyToManyField(to='member.JenisUsaha', blank=True)),
                ('jurusan', models.ForeignKey(blank=True, to='member.Jurusan', null=True)),
                ('keahlian', models.ManyToManyField(to='member.Keahlian', blank=True)),
                ('media', models.ManyToManyField(to='member.Media', blank=True)),
                ('organisasi', models.ManyToManyField(to='member.Organisasi', blank=True)),
                ('pekerjaan', models.ForeignKey(blank=True, to='member.Pekerjaan', null=True)),
                ('pendidikan_terakhir', models.ForeignKey(blank=True, to='member.PendidikanTerakhir', null=True)),
                ('penghasilan_bulanan', models.ForeignKey(blank=True, to='member.PenghasilanBulanan', null=True)),
            ],
            options={
                'verbose_name': 'Anggota',
                'verbose_name_plural': 'Anggota',
            },
        ),
        migrations.CreateModel(
            name='ProgramKB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('program_kb', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Program KB',
                'verbose_name_plural': 'Program KB',
            },
        ),
        migrations.CreateModel(
            name='StatusListrik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_listrik', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Status Listrik',
                'verbose_name_plural': 'Status Listrik',
            },
        ),
        migrations.CreateModel(
            name='StatusPerkawinan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_perkawinan', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Status Perkawinan',
                'verbose_name_plural': 'Status Perkawinan',
            },
        ),
        migrations.CreateModel(
            name='StatusRumah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_rumah', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Status Rumah',
                'verbose_name_plural': 'Status Rumah',
            },
        ),
        migrations.CreateModel(
            name='StatusSosial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('score_min', models.PositiveIntegerField()),
                ('score_max', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Status Sosial',
                'verbose_name_plural': 'Status Sosial',
            },
        ),
        migrations.CreateModel(
            name='SumberAirMinum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sumber_air_minum', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Sumber Air Minum',
                'verbose_name_plural': 'Sumber Air Minum',
            },
        ),
        migrations.CreateModel(
            name='TemaInformasi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tema_informasi', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tema Informasi',
                'verbose_name_plural': 'Tema Informasi',
            },
        ),
        migrations.CreateModel(
            name='Usia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('umur_min', models.PositiveIntegerField()),
                ('umur_max', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Usia',
                'verbose_name_plural': 'Usia',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='status_perkawinan',
            field=models.ForeignKey(to='member.StatusPerkawinan'),
        ),
        migrations.AddField(
            model_name='person',
            name='tema_informasi',
            field=models.ManyToManyField(to='member.TemaInformasi', blank=True),
        ),
        migrations.AddField(
            model_name='handphone',
            name='person',
            field=models.ForeignKey(to='member.Person'),
        ),
        migrations.AddField(
            model_name='family',
            name='jadwal_ronda',
            field=models.ForeignKey(blank=True, to='member.JadwalRonda', null=True),
        ),
        migrations.AddField(
            model_name='family',
            name='jamsos_diterima',
            field=models.ForeignKey(blank=True, to='member.JamsosDiterima', null=True),
        ),
        migrations.AddField(
            model_name='family',
            name='lantai',
            field=models.ForeignKey(to='member.Lantai'),
        ),
        migrations.AddField(
            model_name='family',
            name='program_kb',
            field=models.ForeignKey(blank=True, to='member.ProgramKB', null=True),
        ),
        migrations.AddField(
            model_name='family',
            name='status_listrik',
            field=models.ForeignKey(to='member.StatusListrik'),
        ),
        migrations.AddField(
            model_name='family',
            name='status_rumah',
            field=models.ForeignKey(to='member.StatusRumah'),
        ),
        migrations.AddField(
            model_name='family',
            name='sumber_air_minum',
            field=models.ForeignKey(to='member.SumberAirMinum'),
        ),
    ]
