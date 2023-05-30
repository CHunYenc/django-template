from django.db import models
from apps.utils import TimeStampMixinModel

# Create your models here.


class Version(TimeStampMixinModel):
    """ 系統版本紀錄 """
    version = models.CharField(max_length=10, null=False, unique=True)
    content = models.TextField()
    activate = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = "s_version"
        verbose_name_plural = "System Version - 系統版本歷程記錄"
