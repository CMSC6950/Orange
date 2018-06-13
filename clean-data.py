
# coding: utf-8

# In[ ]:


#this pieac of code gets a dataframe as input and return a cleaned dataframe as outpu

def clean_data(dataframe):
#replacing M to NAN in csv data file
    dataframe.replace('E', np.nan,inplace=True)
#replacing M to NAN in csv data file
    dataframe.replace('M', np.nan,inplace=True)
#Then Remove all the 'NAN' data in csv data file
    data = dataframe.dropna(how='any')
    dataframe=data
    return dataframe
    

