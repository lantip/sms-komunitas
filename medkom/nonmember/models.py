from django.db import models
from smart_selects.db_fields import ChainedForeignKey,GroupedForeignKey

class nonmember(models.Model):
    SEX = (
        (0, 'Laki Laki'),
        (1, 'Perempuan'),
    )
    jenis_kelamin   = models.IntegerField(choices=SEX, default=0)
    nama_lengkap    = models.CharField(max_length=100)
    nama_panggilan  = models.CharField(max_length=20, blank=True)
    no_handphone    = models.CharField(max_length=15, blank=True)
    jabatan         = models.CharField(max_length=255, blank=True)
    nama_dinas      = models.CharField(max_length=255)
    wilayah         = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' %(self.jabatan)
    class Meta:
        verbose_name_plural = 'Non Member'
        verbose_name        = 'Non Member'
