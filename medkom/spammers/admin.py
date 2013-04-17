from spammers.models import *
from django.contrib import admin


class SpammersAdmin(admin.ModelAdmin):
    list_display = ('no_handphone','time')
    search_fields = ['no_handphone']

admin.site.register(Spammers, SpammersAdmin)