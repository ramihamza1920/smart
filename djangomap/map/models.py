from django.contrib.gis.db import models

# Create your models here.

class myProject(models.Model):
    polygon_id = models.BigAutoField(primary_key=True, default=None)
    geomp = models.MultiPolygonField(null=True)
     