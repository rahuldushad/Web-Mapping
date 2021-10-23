
import folium
import pandas

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(Location=[38.5,-99], zoom_start = 6, title = "Mapbox Bright")

fg= folium.FeatureGroup(name="MYmap")
Map.add_child(folium.Marker(Location=[38.2,-99.1]),popup="comment", icon= folium.icon("green"))
map.save(map.html)



data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


html = """
<h4>Volcano name:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

fg = folium.FeatureGroup(name = "Volcanos")


# Use CircleMarker instead of Marker
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe),
                                     fill_color = color_producer(el), color = 'grey', fill_opacity = 0.6))

map.add_child(fg)

fg2 = folium.FeatureGroup(name="Population")
fg2.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                     else 'red'}))
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map with Volcano and Population Info.html")
