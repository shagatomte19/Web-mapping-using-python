import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevator):
    if elevator < 1000:
        return 'green'
    elif 1000 <= elevator < 2000:
        return 'blue'
    elif 2000 <= elevator < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[23.9833,91.1667],zoom_start=4)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el) +" m",fill_color=color_producer(el),color="grey",fill_capacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'blue' if x['properties']['POP2005'] <= 50000000 else 
'yellow' if x['properties']['POP2005'] <= 100000000 else 'orange' if x['properties']['POP2005'] <= 200000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("map1.html")