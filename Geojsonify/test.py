# Import the Geojsonify function and dependencies
from Geojsonify import Geojsonify
from pprint import pprint

# Create a test library for each type of geojson object
point_test = [{
    'place': 'San Diego',
    'mag': 3.2,
    'lat': 32.7157,
    'lng': -117.611
},
{
    'place': 'Rohnert Park',
    'mag': 4.5,
    'lat': 38.3396,
    'lng': -122.7011
},
{
    'place': 'San Francisco',
    'mag': 6.0,
    'lat': 37.7749,
    'lng': -122.4194
},
{
    'place': 'Jacksonville',
    'mag': 3.5,
    'lat': 30.3322,
    'lng': -81.6557
},
{
    'place': 'St. Louis',
    'mag': 5.5,
    'lat': 38.6270,
    'lng': -90.1994
}]

line_test = [{
    'place': 'San Diego',
    'mag': 3.2,
    'latitude': [32.7157, 38.3396],
    'Lng': [-117.611, -122.7011]
},
{
    'place': 'San Diego',
    'mag': 3.2,
    'latitude': [32.7157, 38.3396],
    'Lng': [-117.611, -122.7011]
},
{
    'place': 'San Diego',
    'mag': 3.2,
    'latitude': [32.7157, 38.3396],
    'Lng': [-117.611, -122.7011]
}]

polygon_test = [{
    'place': 'San Diego',
    'mag': 3.2,
    'Lat': [42.68243539838623, 50.62507306341435, 53.9560855309879, 48.69096039092549, 42.68243539838623],
    'Lng': [23.203125, 31.113281249999996, 22.32421875, 16.5234375, 23.203125]
}]

# Test the function
pprint(Geojsonify(point_test, 'Point'))
# pprint(Geojsonify(line_test, 'LineString'))
# pprint(Geojsonify(polygon_test, 'Polygon'))