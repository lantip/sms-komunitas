from django.db import models

class Spammers(models.Model):
    no_handphone = models.CharField(max_length=200)
    time         = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' %(self.no_handphone)

    class Meta:
        verbose_name = "Spammer"
        verbose_name_plural = "Spammer"
