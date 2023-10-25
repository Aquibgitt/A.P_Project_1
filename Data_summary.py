#Data_summary
# Initial step to begin with Importing necessary libraries which are numpy and pandas
import numpy as np
import pandas as pd

#Reading the values to variable dataframe df.
df = pd.read_csv(r'C:\Users\aquib\OneDrive\Desktop\project 1\Crime_Data_from_2020_to_Present.csv') #[https://catalog.data.gov/dataset/crime-data-from-2020-to-present] Please get this data from here as the Dataset is soo large have problems to upload.
class data:
    """
    This class contains all the functions needed for data reading,interpretation and cleaning.
    """
    def __init__(self):
       pass
        
    def details_H():
        """
        Function used to show the first 5 details of the content. 
        """
        return(df.head())
    
    def details_T():
        """
        Function used to show the last 5 details of the content. 
        """
        return(df.tail())
        
    def attributes():
        """
        Function used to show the attributes of dataset.
        """
        return(df.columns)
    
    def info():
        """
        This function shows the details of the attributes such as count of non-null values and data type.
        """
        info = df.info()
        return(info)
    
    def nullvalues():
        """
        Function showing the count of non-null values of each         attributes.
        """
        pd.isnull(df).sum()
        return(nullvalues)
    
    def Missing_values_percentage():
        """
        Function showing the percentage of Missing values of each attributes.
        """
        return((pd.isnull(df).sum()/len(df))*100)
    
    def shape():
        """
        Function showing the dimension of the dataset.
        """ 
        shape = df.shape
        return(shape)
    
    
    def describe():
        """
        Function used to see the statistical summary of data
        """
        describe = df.describe()
        return(describe)
    
    def data_type():
        """
        Function defined to check Data types of the Attributes which we passed 
        """
        data_types = df.dtypes
        return(data_types)