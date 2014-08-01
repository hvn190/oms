__author__ = 'HVN'

from django.db import models
from datetime import datetime

class Project(models.Model):
    type = models.CharField(u'Loai De Tai', max_length=128)
    name = models.CharField(u'Ten De Tai', max_length=128)
    code = models.CharField(u'Ma De Tai', max_length=32)
    date_start = models.DateField(u'Ngay Bat Dau', default=datetime.now())
    date_end = models.DateField(u'Ngay Ket Thuc', default=datetime.now())
    date_report = models.DateField(u'Ngay Bao Cao', default=datetime.now())
    score = models.DecimalField(u'Diem Dat Duoc', decimal_places=1, max_digits=5)
    so_QD = models.CharField(u'So Quyet Dinh',max_length=512 )
    tongkinhphi = models.DecimalField(u'Tong Kinh Phi', decimal_places=3, max_digits=18)





    def __unicode__(self):
        return self.name