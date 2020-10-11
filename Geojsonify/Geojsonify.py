# Import previous functions
from Line_String import line_string
from Point import point
from Polygon import polygon

# Create the Geojsonify Function
# Type is defaulted to Point
def Geojsonify(data, Type='Point'):

    # Determine which function to use
    if Type == 'Point':
        return point(data)

    elif Type == 'LineString':
        return line_string(data)

    elif Type == 'Polygon':
        return polygon(data)

    else:
        print("Error: Type has to be either Point, LineString, or Polygon")  