import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#inputting data
data = pd.read_csv('Life-Expectancy-and-GDP-Starter/all_data.csv')
data.rename(columns={'Life expectancy at birth (years)': 'Expectancy'}, inplace=True)



countries = data.Country.unique()

#DF's by country
chile = data[data.Country == 'Chile']
china = data[data.Country == 'China']
germany = data[data.Country == 'Germany']
mexico = data[data.Country == 'Mexico']
usa = data[data.Country == 'United States of America']
zimbabwe = data[data.Country == 'Zimbabwe'] 

#Line plot of Year v Life Expectancy by Country
def Expectancy_by_country(df, country_list):
    for val in country_list:
        val = df[df.Country == val]
        plt.plot(val.Year, val.Expectancy)
    plt.legend(country_list)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Life Expectancy by Year and Country')
    plt.show()
# Expectancy_by_country(data, countries)

#Line plot of Year v GDP by Country
plt.clf()
def GDP_by_country(df, country_list):
    plt.clf()
    for val in country_list:
        val = df[df.Country == val]
        plt.plot(val.Year, val.GDP)
    plt.legend(country_list)
    plt.xlabel('Year')
    plt.ylabel('GDP * 10e12')
    plt.title('GDP by Year and Country')
    plt.show()
# GDP_by_country(data, countries)

plt.scatter(data.Expectancy, data.GDP, color='orange')
plt.title('Life Expectancy vs. Country GDP')
plt.show()