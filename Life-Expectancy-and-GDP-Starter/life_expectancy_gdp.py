import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import pearsonr

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

#Life Expectancy v GDP scatter
plt.scatter(data.Expectancy, data.GDP, color='orange')
plt.title('Life Expectancy vs. Country GDP')
plt.xlabel('Life Expectancy')
plt.ylabel('GDP')
plt.show()

#correlation of Life Expectancy v GDP
r, pval = pearsonr(data.Expectancy, data.GDP)
print(r, pval)

#all countries Life expectancy v GDP individually plotted
plt.clf()
fig, axs = plt.subplots(3, 2)
axs[0,0].scatter(chile.Expectancy, chile.GDP, color = 'red')
axs[0,0].set_title('Chile')
axs[0,1].scatter(china.Expectancy, china.GDP, color='blue')
axs[0,1].set_title('China')
axs[1,0].scatter(germany.Expectancy, germany.GDP, color='black')
axs[1,0].set_title('Germany')
axs[1,1].scatter(mexico.Expectancy, mexico.GDP, color='green')
axs[1,1].set_title('Mexico')
axs[2,0].scatter(usa.Expectancy, usa.GDP, color='orange')
axs[2,0].set_title('USA')
axs[2,1].scatter(zimbabwe.Expectancy, zimbabwe.GDP, color='pink')
axs[2,1].set_title('Zimbabwe')
for ax in axs.flat:
    ax.set(xlabel='Life Expectancy', ylabel='GDP')
plt.show()

