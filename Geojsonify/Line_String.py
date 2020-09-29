import json

# Create the geojsonify function with the line string format
def line_string(data):
    
    # Initialize the features array
    features = []
    
    # Loop through the list of dictionaries
    for i in range(0, len(data)):
        
        # Initialize lists to store the latitudes and longitudes
        coord1 = []
        coord2 = []
        
        # Loop through each latitude and longitude and append them into the lists
        # Assigne key1 to the lat
        for key1, value1 in data[i].items():
            # Assigne key2 to lng
            for key2, value2 in data[i].items():
                if key1 == 'lat' and key2 == 'lng':
                    # Index through the list of values in each key
                    # lat and lng should have the same number of values in their lists,
                    # so I only need to do the range of the length of one of the lists.
                    for j in range(0, len(data[i][key1])):
                        # value1 == lat
                        value1 = data[i][key1][j]
                        # value2 == lng
                        value2 = data[i][key2][j]
                        # Append to the coord1 and coord2 lists
                        coord1.append(value1)
                        coord2.append(value2)
         
        # Use list comprehension to create a list of lists that contain the coordinate pairs as (lng, lat)
        coordinates = [[coord2[i], coord1[i]] for i in range(0, len(coord1))]
                
        
        # Loop through the key and values to populatate a new dictionary called properties
        # Excluding the lat and lng
        properties = {key: value for key, value in data[i].items() if key != "lat" and key != "lng"}
        
        # Create the key and values that will populate the features array
        my_features = {
            "type": "Feature",
            "properties": properties,
            "geometry": {
                "type": "LineString",
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