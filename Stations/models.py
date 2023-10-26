from django.db import models
#from region.models import Region
#from Gov_Region.models import Region_Governrate
from governorate.models import Governorate


class stations(models.Model):

    idS = models.IntegerField(unique=True)
    operationCode = models.IntegerField(unique=True)
    governorate_id = models.ForeignKey(
        Governorate, on_delete=models.CASCADE, related_name="Gov_id", null=False)
    name = models.JSONField(null=False)
    IsActive = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "stations"
