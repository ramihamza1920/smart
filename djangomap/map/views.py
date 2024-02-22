from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from .models import myProject
# from django.contrib.gis.serializers import serialize

def map(request):        
    if request.method == 'POST':
        multiPolygone = request.POST.get('points')
        multipolygon = GEOSGeometry(multiPolygone, srid=4326)
        forme = myProject(geomp=multipolygon)
        forme.save()  
        print("Forme ajoutée à la base de données")

    # Récupérer toutes les formes stockées dans la base de donnée
    return render(request, "map/map.html")

