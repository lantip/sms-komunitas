from member.models import Person, Family, Handphone, KeluargaGangguan, JenisDifable, StatusRumah
from member.models import Lantai, Dinding, Atap, JamsosDiterima, SumberAirMinum, StatusListrik
from member.models import DayaListrik, JadwalRonda, ProgramKB, Agama, StatusPerkawinan, HubunganKeluarga
from member.models import PendidikanTerakhir, Jurusan, Pekerjaan, GolonganDarah, PenghasilanBulanan, Hobi
from member.models import Keahlian, JenisUsaha, Organisasi, Media, TemaInformasi, AlatTransportasi
from member.models import Usia, StatusSosial
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
        depth = 1

class StatusPerkawinanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPerkawinan
        fields = '__all__'

class GolonganDarahSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolonganDarah
        fields = '__all__'

class AgamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agama
        fields = '__all__'

class UsiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usia
        fields = '__all__'

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100