import json

# Create the geojsonify function with the line string format
# Create the geojsonify function with the line string format
def polygon(data):
    
    # Initialize the features array
    features = []
    
    # Create lists of possible names and abbrev. for latitude and longitude
    latitude = ['lat', 'latitude', 'Lat', 'Latitude']
    longitude = ['lng', 'longitude', 'Lng', 'Longitude']
    
    # Loop through the list of dictionaries
    for i in range(0, len(data)):
        
        # Initialize lists to store the latitudes and longitudes
        coord1 = []
        coord2 = []
        
        # Create functions to determine if the key is latitude or longitude
        def is_coord(key, data_list):
            for i in range(0, len(data_list)):
                if key == data_list[i]:
                    return data_list[i]
        
        # Loop through each latitude and longitude and append them into the lists
        # Assigne key1 to the lat
        for key1, value1 in data[i].items():
            # Assigne key2 to lng
            for key2, value2 in data[i].items():
                if key1 == is_coord(key1, latitude) and key2 == is_coord(key2, longitude):
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
        coordinates_1 = [[coord2[i], coord1[i]] for i in range(0, len(coord1))]
        # Put the list of lists in another list for proper formatting
        coordinates = [coordinates_1]
                
        
        # Loop through the key and values to populatate a new dictionary called properties
        # Excluding the lat and lng
        properties = {key: value for key, value in data[i].items() if key != is_coord(key, latitude) and key != is_coord(key, longitude)}
        
        # Create the key and values that will populate the features array
        my_features = {
            "type": "Feature",
            "properties": properties,
            "geometry": {
                "type": "Polygon",
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