import folium
import pandas
import csv


map2017 = folium.Map(location=[-25, 30],
                     zoom_start=5,
                     tiles='OpenStreetMap')
map2018 = folium.Map(location=[44, 51],
                     zoom_start=5,
                     tiles='OpenStreetMap')

folium_map = map2018

with open('2018.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            marker = folium.Marker(location=[float(row[2]), float(row[1])],
                                   popup=row[0])
            marker.add_to(folium_map)
            line_count += 1
    print(f'Processed {line_count} lines.')
folium_map.save("2018.html")
