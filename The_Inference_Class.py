#The_Inference_Class
import numpy as np 
import pandas as pd 
#Importing the Visualization libraries
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings('ignore')
import EDA_FILE

#Reading the values and storing it in a dataframe using pandas
df = pd.read_csv(r'C:\Users\aquib\OneDrive\Desktop\project 1\Crime_Data_from_2020_to_Present.csv') #[https://catalog.data.gov/dataset/crime-data-from-2020-to-present] Please get this data from here as the Dataset is soo large have problems to upload.
class inference_analysis:
    """
    This class contains the function to analyse and get the conclusions of the research question.
    """
    def __init__(self):
       pass
    

    def Result_1():
        """
        The visualization highlights the critical analysis of reported crimes based on their descriptions and the time of day. This information is invaluable for law enforcement, enabling better resource allocation and tailored patrols during peak crime hours. It aids in developing targeted crime prevention strategies, such as enhanced security in retail stores when shoplifting is more likely. 
        Policymakers can utilize this data to enact effective regulations, like stricter controls on alcohol sales during high-crime periods. Community members can stay informed and take precautions during times when specific crimes are more prevalent, fostering a safer environment.
        The highest crime which was reported is in the evening which is battery simple assault , however there are many crimes which are counted enormously like there is a complex and many crimes.shoplifting petty theft comes next.
        """
        time_zone_order = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night']
        data_frame = EDA_FILE.EDA_Exploration.Binning()
        #Setting up the figure size
        plt.figure(figsize=(30, 15))
        #Using the Counterplot with set2 pallette and using hue for colour encoding.
        sns.countplot(data=data_frame, x='Time Zone', hue='Crm Cd Desc', order= time_zone_order, palette='Set2', dodge=True)
        plt.xlabel('Time Zone',size = 30)
        plt.ylabel('Count of Reported Crimes',size= 30)
        plt.title('Reported Crimes by Time Zone and Crime Description',size = 40)
        #with the custom rotation we can tilt out titles to any angle 
        plt.xticks(rotation=0)
        #By giving the loc on upper left we are managing not to make the fig soo Conjested.
        plt.legend(title='Crime Description', title_fontsize='30', loc='upper left', bbox_to_anchor=(1.15, 1))
        plt.show()


    def Result_2():

        """
        In our project, we're delving into the fascinating realm of crime analysis to unravel the connection between age groups and the types of crimes committed. This is a vital piece of the puzzle for crafting effective crime prevention strategies tailored to different demographics. Our analysis was brought to life through an impressive heatmap, which showcases the correlation between age groups and crime descriptions. 
        The color variations help us pinpoint which crimes have a stronger association with specific age groups.
        You might wonder why certain crimes are more prevalent among particular age groups.
        Well, this could be due to various factors, such as vulnerabilities or opportunities unique to each age group. What's particularly intriguing is that our data reveals that adults are the primary victims. This suggests that they are more exposed to a wide range of situations that make them potential targets.
        Furthermore, one standout finding is the high frequency of battery assault across all age groups. This could indicate that this type of crime is a common occurrence in society. To truly combat it, we need to dive deeper into its root causes and devise effective preventative measures. This endeavor is not only intriguing but also essential in enhancing our understanding of crime patterns and, ultimately, improving public safety."
        Coming to the Code we used the groupby function to gather the age group and the crime descriptions altogather showing the figure size
        """
        data_frame = EDA_FILE.EDA_Exploration.Binning()
        # Correlation between age group and crime description.
        # Create a pivot table to count occurrences of each age group and crime description with the Heat Map.
        correlation_data = data_frame.groupby(['Age_Group', 'Crm Cd Desc']).size().unstack(fill_value=0)

        ## Setting the figure size and DPI for better resolution (We can change the size of figure anytime needed)
        plt.figure(figsize=(70, 20), dpi=100)

        # Create a heatmap with a different color palette 
        sns.heatmap(correlation_data, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Count'})
        plt.title('Correlation Between Age Groups and Crime Descriptions',size = 40)
        plt.xlabel('Crime Description',size = 40)
        plt.ylabel('Age_Group',size = 40)

        plt.show()

    def Result_3():

        """
        The graph Below is a powerful visual representation of the intricate relationship between specific crime types and geographical areas. We've meticulously calculated the correlation between different crime descriptions and various areas. 
        This rich heatmap showcases the patterns, with varying colors denoting the strength of these correlations.
        Why is this significant, you ask? Well, understanding which areas are notorious for specific types of crimes is a crucial step in developing effective crime prevention and law enforcement strategies. 
        By identifying these correlations, law enforcement agencies can allocate their resources more efficiently, and policymakers can tailor their approaches to address the specific needs of each area.
        As for the graph itself, the colors on the heatmap provide a quick and intuitive way to grasp the variations in crime occurrences across different areas. Brighter spots indicate a stronger association between a particular crime type and an area,
        while darker areas suggest a weaker correlation. This visual representation is an invaluable tool for anyone seeking to enhance public safety and address the unique challenges posed by crime in different neighborhoods.
        """

        # Calculate the correlation between crime types and areas,even here we are using the groupby between the areas and crime descriptions
        
        crime_area_correlation = df.groupby(['Crm Cd Desc', 'AREA']).size().unstack(fill_value=0)

        # Setting the figure size and DPI for better resolution
        plt.figure(figsize=(60, 40))

        # Create a heatmap with a different color palette
        sns.heatmap(crime_area_correlation, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Count'})
        plt.title('Correlation Between Crime Types and Areas', size=15)
        plt.xlabel('Area', size=12)
        plt.ylabel('Crime Description', size=12)
        plt.show()

    def Result_4():

        """
        In this code we are looking for the same correlation by picking the Top-5 Crimes ,so that it would be much convenient.
        """
       # Calculate the top 5 crime types
        top_crimes = df['Crm Cd Desc'].value_counts().head(5).index

        # Filter the DataFrame to include only the rows with the top 5 crime types
        filtered_df = df[df['Crm Cd Desc'].isin(top_crimes)]

        # Calculate the correlation between the filtered crime types and areas
        crime_area_correlation = filtered_df.groupby(['Crm Cd Desc', 'AREA']).size().unstack(fill_value=0)

        # Setting the figure size and DPI for better resolution
        plt.figure(figsize=(30, 20))

        # Create a heatmap with a different color palette
        sns.heatmap(crime_area_correlation, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Count'})
        plt.title('Correlation Between Top 5 Crime Types and Areas', size=15)
        plt.xlabel('Area', size=12)
        plt.ylabel('Crime Description', size=12)
        plt.show()
