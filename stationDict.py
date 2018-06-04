
# coding: utf-8

# In[1]:


#This function maps given city name to its station ID 
#city name will be given as input and corresponding station ID will be found in dictionary and returned

def city_to_stationID(ncity):
    stations = {'St. John\'s': 50089, 
                'Yellowknife': 51058,
                'Charlottetown': 50621, 
                'Halifax': 50620,
                'Fredericton': 48568, 
                'Ottawa': 49568,
                'Winnepeg': 51097,
                'Regina': 28011,
                'Edmonton': 50149,
                'Victoria': 51337,
                'Quebec City': 26892,
                'Whitehorse': 50842,
                'Montreal':51157,
                'Iqaluit': 42503}
    return stations[ncity]

