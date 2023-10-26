from django.db import models
from branches.models import branch
from Stations.models import stations

class branch_station (models.Model):
    idx = models.IntegerField()
    branch_id = models.ForeignKey(branch, on_delete=models.CASCADE,related_name='branch_station')
    station_id = models.ForeignKey(stations , on_delete=models.CASCADE)
    KM = models.FloatField()
    #wait =models.TimeField()
    #time = models.IntegerField()

    class Meta:
         unique_together = (('branch_id','idx'),)
         db_table = "branch_station"

"""def __str__(self):
    return self.primary_key"""
