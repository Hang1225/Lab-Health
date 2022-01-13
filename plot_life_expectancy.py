import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# variable declaration

class life_expectancy:
    NA_male  = []
    NA_female = []
    Asia_male = []
    Asia_female = []

male = pd.read_csv('Resources/Life_Expectancy_Male.csv',skiprows=3)
female = pd.read_csv('Resources/Life_Expectancy_Female.csv',skiprows=3)
#drop unncessary columns
male.drop(['Indicator Name','Indicator Code','2020','Unnamed: 65'],axis=1,inplace=True)
female.drop(['Indicator Name','Indicator Code','2020','Unnamed: 65'],axis=1,inplace=True)
#delete any rows with NaN values
male.dropna(axis=0,inplace=True)
female.dropna(axis=0,inplace=True)

le = life_expectancy
#get NA Data
le.NA_male = male[male['Country Code'] == 'NAC']
le.NA_female = female[female['Country Code'] == 'NAC']

#get Asia Data
le.Asia_male = male[male['Country Code'] == 'EAS']
le.Asia_female = female[female['Country Code'] == 'EAS']

column_name = male.columns[2:] # x-axis data

#Plotting

fig, axs = plt.subplots(nrows = 2, ncols = 1, constrained_layout=False,figsize = (10,10)) #create subplot
fig.tight_layout(pad=5.0) # set spacing between subplots
# plotting NA data
axs[0].scatter(x=column_name,y=le.NA_male.to_numpy()[0][2:],label='Male')
axs[0].scatter(x=column_name,y=le.NA_female.to_numpy()[0][2:],marker = 'D',label='Female')
axs[0].set_title('Life Expectancy in North America by Gender',fontsize = 14)
axs[0].set_ylabel('Life Expectancy (years)')

axs[0].legend(loc=0) # set legend location
axs[0].set_xticks(column_name[::2]) # change x-tick interval to 2, reduce cluttering
axs[0].set_xticklabels(column_name[::2],rotation=90) #rotate x axis label to prevent clutter.
axs[0].text(59.5,76.5,round(le.NA_female['2019'].iloc[0])) # data label for female
axs[0].text(59.5,81.5,round(le.NA_male['2019'].iloc[0])) # data label for male
# plotting Asia data
axs[1].scatter(x=column_name,y=le.Asia_male.to_numpy()[0][2:],label='Male')
axs[1].scatter(x=column_name,y=le.Asia_female.to_numpy()[0][2:],marker = 'D',label='Female')
axs[1].set_title('Life Expectancy in East Asia & Pacific by Gender',fontsize = 14)
axs[1].set_ylabel('Life Expectancy (years)')

axs[1].legend(loc=0) # set legend location
axs[1].set_xticks(column_name[::2]) # change x-tick interval to 2, reduce cluttering
axs[1].set_xticklabels(column_name[::2],rotation=90) #rotate x axis label to prevent clutter.
axs[1].text(59.5,78.5,round(le.Asia_female['2019'].iloc[0])) # data label for female
axs[1].text(59.5,73.5,round(le.Asia_male['2019'].iloc[0])) # data label for male

plt.show()