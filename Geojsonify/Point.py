# Import json in order to convert python dictionaries to json strings
import json

# Geojson is a format for encoding geographical data into json (JavaScript Object Notation)

# Create the geojsonify function that will convert python dictionaries to point form geojson objects
def point(data):
    
    # Initialize the features array
    features = []
    
    # Create lists of possible names and abbrev. for latitude and longitude
    latitude = ['lat', 'latitude', 'Lat', 'Latitude']
    longitude = ['lng', 'longitude', 'Lng', 'Longitude']
    
    # Loop through the list of dictionaries
    for i in range(0, len(data)):
        
        # Create functions to determine if the key is latitude or longitude
        def is_coord(key, data_list):
            for i in range(0, len(data_list)):
                if key == data_list[i]:
                    return data_list[i]
        
        # List comprehension to grab the coordinates in the order of longitude, latitude
        # The function sorted() uses a keyword 'reverse' that when set to true will reverse the order
        coordinates = [value for key, value in sorted(data[i].items(), reverse=True) if key == is_coord(key, longitude) or key == is_coord(key, latitude)]
        
        # Loop through the key and values to populatate a new dictionary called properties
        # Excluding the lat and lng
        properties = {key: value for key, value in data[i].items() if key != is_coord(key, latitude) and key != is_coord(key, longitude)}
        
        # Create the key and values that will populate the features array
        my_features = {
            "type": "Feature",
            "properties": properties,
            "geometry": {
                "type": "Point",
                "coordinates": coordinates
            }
        }
        
        # Append to the features array
        features.append(my_features)
        
    # Create a new dictionary that will be the format for the geojson object
    new_data = {
        "type": "FeatureCollection",
        "features": features
    }
    
    
    # Function returns the json object
    return json.dumps(new_data)