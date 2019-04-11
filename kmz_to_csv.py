from bs4 import BeautifulSoup

inputfile = "my_places.kml"
with open(inputfile, 'r') as f:
    soup = BeautifulSoup(f)

    # After you have a soup object, you can access tags very easily.
    # For instance, you can iterate over and get <description> like so:
    name = []
    coords = []
    datetime = []
    joined = []

    for node in soup.select('name'):
        if 'My Places' not in node:
            name.append(str(node))

    for node in soup.select('coordinates'):
        coords.append(str(node))

    for node in soup.select('TimeStamp'):
        datetime.append(str(node))

    for i in range(len(name)):
        namestr = name[i].strip('<name>')
        namestr = namestr.strip('</name>')
        
        datestr = datetime[i].strip('<TimeStamp><when>')
        datestr = datestr.strip('</when></timestamp>')
        datestr = datestr[0:10]

        coordstr = coords[i].strip('<Point><coordinates>')
        coordstr = coordstr.strip('</coordinates></Point>')

        joined.append(namestr + ' ' + datestr + ', ' + coordstr)
    
for i in joined:
    with open('my_places.csv', 'a') as f:
        f.write(i + '\n')
