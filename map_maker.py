import folium
import pandas
import csv

folium_map = folium.Map(location=[40, 51],
            zoom_start=5,
            tiles='OpenStreetMap')
with open('my_places.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count+=1
        else:
            marker = folium.Marker(location=[float(row[2]), float(row[1])],
                                    popup=row[0])
            marker.add_to(folium_map)
            line_count+=1
    print(f'Processed {line_count} lines.')
folium_map.save("my_map.html")
