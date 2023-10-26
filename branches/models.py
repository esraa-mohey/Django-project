from django.db import models

class branch (models.Model):
    name = models.JSONField(null=False)
    #ar_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
      return self.name

    class Meta:
        db_table = "branch"      
