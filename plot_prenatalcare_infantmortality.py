import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

########## Read CSVs into separate dateframes ##########
infant_mortality = pd.read_csv(r'Resources\Mortality_Infant.csv',skiprows=4)
prenatal_care = pd.read_csv(r'Resources\Prenatal_Care.csv',skiprows=4)

########## Clean dataframes ##########
exclude_codes = ['WLD', 'LAC', 'LCN', 'NAC', 'TLA', 'CEB', 'ECA', 'ECS', 'EU', 'TEC', 'EAP', 'EAS', 'SAS', 'TEA', 'TSA', 'MEA', 'MNA', 'SSA', 'SSF', 'TMN', 'TSS', 'ZAF', 'AFE', 'AFW', 'CAF']

infant_mortality = infant_mortality[~infant_mortality['Country Code'].isin(exclude_codes)]
infant_mortality = infant_mortality[['Country Name','2000']]
infant_mortality = infant_mortality.rename(columns={'2000':'Infant Mortality'})
infant_mortality = infant_mortality.dropna()

# infant_mortality.info()
# print(infant_mortality)


prenatal_care = prenatal_care[~prenatal_care['Country Code'].isin(exclude_codes)]
prenatal_care = prenatal_care[['Country Name','2000']]
prenatal_care = prenatal_care.rename(columns={'2000':'Prenatal Care'})
prenatal_care = prenatal_care.dropna()

# prenatal_care.info()
# print(prenatal_care)

########## Merge dataframes ##########
merged = infant_mortality.merge(prenatal_care,how='inner',on='Country Name')

# merged.info()
# print(merged)

########## Plot Prenatal care vs Infant mortality ##########
x = merged['Prenatal Care']
y = merged['Infant Mortality']

# Line of best fit
m, b = np.polyfit(x,y,1)
plt.plot(x, m*x + b, color = 'black')

# R ^ 2
correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0, 1]
r_squared = correlation_xy**2

plt.scatter(x, y)
plt.xlabel('Pregnant women recieving prenatal care (%)')
plt.ylabel('Mortality rate, infant (per 1,000 live births)')
plt.title('Infant Mortality Rate vs Pregnant Women Recieving Prenatal Care')

#Showing text: the number are the x and y values to start showing the text, respectively
plt.text(38, 2, f"y = {round(m,4)}x + {round(b,2)}, $r^2$ = {round(r_squared,2)}", fontsize = 12)

# plot = merged.plot(title = 'Pregnant women recieving prenatal care (%) vs Mortality rate, infant (per 1,000 live births)',kind='scatter',x='Prenatal Care',y='Infant Mortality')
# plot.set_xlabel('Pregnant women recieving prenatal care (%)')
# plot.set_ylabel('Mortality rate, infant (per 1,000 live births)')

plt.show()