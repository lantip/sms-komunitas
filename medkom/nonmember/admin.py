from nonmember.models import *
from django.contrib import admin


class NonMemberAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'no_handphone', 'jabatan', 'nama_dinas', 'wilayah')
    search_fields = ['nama_lengkap', 'nama_panggilan', 'jabatan', 'nama_dinas']

admin.site.register(nonmember, NonMemberAdmin)