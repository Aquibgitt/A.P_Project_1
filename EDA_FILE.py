#Project-1 EDA FILE
## First and foremost thing to do is Importing the PYTHON libraries.

import numpy as np 
import pandas as pd 
#Importing the Visualization libraries
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings('ignore')
#Reading the values and storing it in a dataframe using pandas
df = pd.read_csv(r'C:\Users\aquib\OneDrive\Desktop\project 1\Crime_Data_from_2020_to_Present.csv') #[https://catalog.data.gov/dataset/crime-data-from-2020-to-present] Please get this data from here as the Dataset is soo large have problems to upload.

class EDA_Exploration:
    """
    This class encompasses various functions dedicated to conducting exploratory data analysis,
    facilitating comparisons among different attributes, and presenting the findings through diverse visualizations created with the Matplotlib and Seaborn libraries.
    The ultimate goal is to draw insightful conclusions derived from the visual representations.
    """
    def __init__(self):
       pass

    def Cleaning():
        """
        After checking the Missing
        and the Null values percentages we are dropping the columns which has most missing values which could disturb the dataset
        So, firstly we are removing the missing values from the columns and later we are removing the Rows with missing values from the dataset 
        Make sure to crosscheck the shape and columns of the dataset,to make sure if everything is cleared.Please call the null values percentage too for confirmation.

        """
        #drop unrelated/blank columns, and using inplace to commit and avoid the extra memory occupancy
        df.drop(['Date Rptd','Mocodes', 'DR_NO','Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3' ,'Crm Cd 4','Cross Street','Weapon Used Cd','Weapon Desc','Part 1-2','LAT','LON'],axis=1, inplace=True)
        #To remove missing values from the rows
        df.dropna(axis=0)
        return(df)

    def Outlier_check():
        """
        We incorporated these dual side-by-side box plots to delve into our data, seeking outlying data points and uncovering the medians. The box plots help us visualize these aspects effectively.
        In our 'Vict Age' box plot, we noticed a few data points that stand out as outliers, mostly on the higher age side. These outliers represent a small group of unusually older victims, which could be of interest for further investigation.
        Likewise, the 'TIME OCC' box plot revealed outliers at the upper end, indicating some uncommon instances of late occurrences. These outliers are valuable in identifying patterns in the data, such as potential nighttime incidents.
        In both box plots, the boxes themselves represent the interquartile range (IQR), providing insights into the middle 50% of the data. The horizontal line inside each box marks the median, signifying the midpoint of the data distribution for each attribute.
        This analysis helps us understand the central tendencies and the presence of any extreme data points. 
        """
        #Box Plot for determining victim's age
        plt.subplot(1,2,1)
        sns.boxplot(df['Vict Age'])
        plt.xlabel('Vict Age')

        #Box plot for determining Time
        plt.subplot(1,2,2)
        sns.boxplot(df['TIME OCC'])
        plt.xlabel('Time OCC')
        #This is to show the visualization.
        plt.show() 
        ##df is the Dataframe in which we read all the data.

    def Binning():
        """
        In this example, we convert the "TIME OCC" values to datetime objects using the pd.to_datetime function and then extract the time part. We define the bin edges and labels for the time zones and use pd.cut to create a new column "Time Zone" based on these bins.
         The resulting DataFrame will have a new column "Time Zone" with values indicating the time zone for each time value. You can adapt the bin edges and labels to suit your specific time zone definitions.
         similarly we used the Binning for age group ,so that we make 6 age groups according to the age group.
        """
        bin_edges = [0,400,500, 1200, 1800, 2400]
        bin_labels = ['Early Morning','Morning', 'Afternoon', 'Evening','Night']

        # Create a new column by binning the 'TIME OCC' column
        df['Time Zone'] = pd.cut(df['TIME OCC'], bins=bin_edges, labels=bin_labels)

        #Now Binning the Age column to find out the Age group of Victims.
        bin_edges = [0,12,25,40 ,60 ,100]
        bin_labels = ['Children','Teen', 'Adult', 'Middle-Adult','Old']

        # Create a new column by binning the 'TIME OCC' column
        df['Age_Group'] = pd.cut(df['Vict Age'], bins=bin_edges, labels=bin_labels)   
        return(df)
    def Crime_by_Time():
        """
        The variation in the number of reported crimes throughout the day reveals distinct temporal patterns. 
        Notably, the evening records the highest count of crimes, while the morning exhibits the lowest.
        This fluctuation can be attributed to factors such as activity patterns, visibility, daily routines, police presence, and economic and social influences.
        The evening, often marked by increased human activity and reduced visibility, becomes a prime time for criminal activities. Conversely, mornings, characterized by routines and greater visibility, serve as a deterrent.
        Understanding these temporal crime patterns is pivotal for law enforcement and policymakers, aiding in the efficient allocation of resources and the development of targeted crime prevention strategies
        """
        # Define the order of time zones for plotting (I named 4 categories in a Day as Time Zone.)
        time_zone_order = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night']

        # Create a figure with two subplots
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Subplot 1: Matplotlib Bar Plot
        time_zone_counts = df['Time Zone'].value_counts().loc[time_zone_order]
        axes[0].bar(time_zone_counts.index, time_zone_counts.values, color='skyblue')
        axes[0].set_xlabel('Time Zone')
        axes[0].set_ylabel('Count of Reported Crimes')
        axes[0].set_title('Matplotlib - Reported Crimes by Time Zone')
        axes[0].tick_params(axis='x', rotation=0)

        # Subplot 2: Seaborn Count Plot
        sns.countplot(data=df, x='Time Zone', order=time_zone_order, palette='pastel', ax=axes[1])
        axes[1].set_xlabel('Time Zone')
        axes[1].set_ylabel('Count of Reported Crimes')
        axes[1].set_title('Seaborn - Reported Crimes by Time Zone')

        plt.tight_layout()  # Adjusts spacing between subplots
        plt.show()

    def Crime_by_Gender(): 
        """
        In this code, we've crafted a comprehensive visualization that encapsulates the demographics of crime victims, distinctly highlighting gender disparities across age groups.
        Leveraging both Matplotlib and Seaborn, we efficiently depicted these patterns. Notably, our data unravels that adult populations exhibited a gender-neutral distribution of crime victims. 
        However, within the middle-aged group, males experienced a higher incidence of crimes compared to their female counterparts. Conversely, in the younger age brackets, particularly among teens and children, females bore a more substantial brunt of criminal activities.
        This multifaceted representation is the result of meticulous data grouping by 'Age_Group' and 'Vict Sex', enabling us to present the findings through distinct bar plots. These visualizations convey valuable insights, reinforcing the intricate interplay between age and gender in the realm of victimization
        """   
                # Create a figure with two subplots
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Group the data by 'Age_Group' and 'Vict Sex' and count the occurrences
        grouped_data = df.groupby(['Age_Group', 'Vict Sex']).size().unstack()

        # Define colors for males and females
        colors = ['skyblue', 'lightcoral']

        # Plot the data for males and females using Matplotlib
        for i, (label, color) in enumerate(zip(grouped_data.columns, colors)):
            axes[0].bar(grouped_data.index, grouped_data[label], label=label, color=color)

        # Add labels and title for Matplotlib subplot
        axes[0].set_xlabel('Age_Group')
        axes[0].set_ylabel('Count')
        axes[0].set_title('Male and Female Populations by Age Group (Matplotlib)')
        axes[0].legend(title='Vict Sex')

        # Create a count plot using Seaborn on the second subplot
        sns.countplot(data=df, x='Age_Group', hue='Vict Sex', palette='pastel', ax=axes[1])
        axes[1].set_xlabel('Age_Group')
        axes[1].set_ylabel('Count')
        axes[1].set_title('Male and Female Populations by Age Group (Seaborn)')

        # Adjust layout to prevent overlap
        plt.tight_layout()

        # Show the subplots
        plt.show()

    def Crime_by_Area():
        """
        Overall purpose of this Graph is to show the count of the occurrences of Crimes across Different areas, showing the Highest number of count per area. 
        and the results are stored in a new DataFrame called area_crime_counts with columns 'AREA' and 'Count'.
        Certainly! In the given dataset, the area with the highest count of reported crimes is labeled as the "most notorious" area. This designation is based on the 'AREA' column, where the area name associated with the highest count of reported crimes is identified. 
        It signifies the region or neighborhood where law enforcement and local authorities might face significant challenges related to crime and public safety. The most notorious area often requires specific attention in terms of resource allocation, community policing,
        and targeted crime prevention strategies to address the prevalent issues and improve overall safety.
        """
         # Create a DataFrame for the counts of reported crimes by area
        area_crime_counts = df['AREA'].value_counts().reset_index()
        area_crime_counts.columns = ['AREA', 'Count']

        # Find the area with the highest count
        most_notorious_area = area_crime_counts.loc[area_crime_counts['Count'].idxmax()]

        # Create a figure with two subplots
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Plot using Matplotlib
        axes[0].bar(area_crime_counts['AREA'], area_crime_counts['Count'], color='skyblue')
        axes[0].set_xlabel('Area')
        axes[0].set_ylabel('Count of Reported Crimes')
        axes[0].set_title('Reported Crimes by Area (Matplotlib)')
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].text(most_notorious_area['AREA'], most_notorious_area['Count'], f'Most Notorious Area: {most_notorious_area["AREA"]}', ha='center', va='bottom', color='red')

        # Plot using Seaborn
        sns.barplot(data=area_crime_counts, x='AREA', y='Count', ax=axes[1])
        axes[1].set_xlabel('Area')
        axes[1].set_ylabel('Count of Reported Crimes')
        axes[1].set_title('Reported Crimes by Area (Seaborn)')
        axes[1].tick_params(axis='x', rotation=45)
        axes[1].text(most_notorious_area['AREA'], most_notorious_area['Count'], f'Most Notorious Area: {most_notorious_area["AREA"]}', ha='center', va='bottom', color='red')

        # Show the combined plot
        plt.tight_layout()
        plt.show()

        # Display the most notorious area
        print(f"The most notorious area for crimes is {most_notorious_area} (Area {most_notorious_area['AREA']}) with {most_notorious_area['Count']} reported crimes.")   

    def Crime_by_years():        
        """
        In this plot, we first convert the "DATE OCC" column to datetime format, extract the year and month information, and then create a histogram using Seaborn.
        The histogram is stacked by month, allowing you to visualize the reported times grouped by year and month.
        Convert 'DATE OCC' to datetime, The crime rate was comparitively lower in the beginning of 2020 while it reached to 2022 the crime rate reached to its peaks. 
        """
        df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
        # Extract year and month
        df['Year'] = df['DATE OCC'].dt.year
        df['Month'] = df['DATE OCC'].dt.month
        # Create a histogram using Seaborn
        plt.figure(figsize=(15, 6))
        sns.histplot(data=df, x='Year', hue='Month', discrete=(True, False), multiple='stack', palette='flare')
        plt.title('Reported Times by Year and Month')
        plt.xlabel('Year')
        plt.ylabel('Count of Reported Times')
        plt.show()


    def Crime_line_years():
        """
        We tried to implement this line of code to visualize this as a line graph both in seaborn and Matplotlib.
        """   
        # Calculate counts of reported times by year and month
        counts = df.groupby(['Year', 'Month']).size().reset_index(name='Count')

        # Create a figure with two subplots
        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)  # First subplot for Matplotlib

        # Matplotlib line plot
        plt.plot(counts['Year'], counts['Count'], label='Counts', marker='o', color='b', linestyle='-', linewidth=2)
        plt.title('Reported Times by Year and Month (Matplotlib)')
        plt.xlabel('Year')
        plt.ylabel('Count of Reported Times')
        plt.grid(True)

        plt.subplot(1, 2, 2)  # Second subplot for Seaborn

        # Seaborn line plot
        sns.lineplot(data=counts, x='Year', y='Count', marker='o', color='b', linewidth=2)
        plt.title('Reported Times by Year and Month (Seaborn)')
        plt.xlabel('Year')
        plt.ylabel('Count of Reported Times')
        plt.grid(True)

        # Show the plots
        plt.tight_layout()  # Ensures the plots don't overlap
        plt.show()

    def Crime_by_Count():
        """
        The provided code presents a visual comparison of the top 5 most frequent crimes based on their descriptions using both Matplotlib and Seaborn libraries. This side-by-side representation allows for a direct evaluation of the crime data. In the Matplotlib subplot, the top crimes are displayed using a bar plot, where the crime descriptions are on the x-axis and the corresponding counts on the y-axis.
        The Seaborn subplot follows the same approach, presenting the same data using a different color palette. and In this code the type of crime which we saw the most is Battery simple assualtfollowing with other crimes.
        """
        top_crimes_desc = df.groupby(['Crm Cd Desc']).size().reset_index(name='Count').sort_values(by='Count', ascending=False).head(5)

        # Top 5 Most Frequent Crimes by Description
        plt.figure(figsize=(15, 6))

        # Matplotlib bar plot
        plt.subplot(1, 2, 1)
        plt.bar(top_crimes_desc['Crm Cd Desc'], top_crimes_desc['Count'], color='lightseagreen')
        plt.title('Top 5 Most Frequent Crimes (Description)')
        plt.xlabel('Crime Description')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')

        # Seaborn bar plot
        plt.subplot(1, 2, 2)
        sns.barplot(data=top_crimes_desc, x='Crm Cd Desc', y='Count', palette='Set1')
        plt.title('Top 5 Most Frequent Crimes (Description)')
        plt.xlabel('Crime Description')
        plt.ylabel('Count')
        plt.xticks(rotation=45)

        plt.tight_layout()  # Ensures the plots don't overlap

        plt.show()






    