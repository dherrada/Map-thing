from bs4 import BeautifulSoup

inputfile = "my_places1.kml"
with open(inputfile, 'r') as f:
    soup = BeautifulSoup(f)

    # After you have a soup object, you can access tags very easily.
    # For instance, you can iterate over and get <description> like so:
    name = []
    coords = []
    datetime = []
    joined = []

    for node in soup.select('name'):
        if 'My Places' and 'My Places1' not in node:
            name.append(str(node))

    for node in soup.select('coordinates'):
        coords.append(str(node))

    for node in soup.select('TimeStamp'):
        datetime.append(str(node))

    for i in range(len(name)):
        namestr = name[i].replace('<name>', '')
        namestr = namestr.replace('</name>', '')

        datestr = datetime[i].replace('<TimeStamp><when>', '')
        datestr = datestr.replace('</when></timestamp>', '')
        datestr = datestr.replace('<timestamp><when>', '')
        datestr = datestr[0:10]

        coordstr = coords[i].replace('<Point>', '')
        coordstr = coordstr.replace('</Point>', '')
        coordstr = coordstr.replace('<coordinates>', '')
        coordstr = coordstr.replace('</coordinates>', '')

        joined.append(namestr + ' ' + datestr + ', ' + coordstr)

for i in joined:
    with open('my_places.csv', 'a') as f:
        f.write(i + '\n')
