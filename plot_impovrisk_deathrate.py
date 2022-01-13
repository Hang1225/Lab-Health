import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------------------------------------------------------------
### Extraction ###
impov=pd.read_csv(r'Resources\Risk_Impoverishing_Expenditures.csv',skiprows=4)
death=pd.read_csv(r'Resources\Deathrate_crude.csv',skiprows=4)

### Transformation ###
impov=impov[['Country Name','Country Code','2018']]
impov=impov[~impov['2018'].isna()]
impov.rename(columns={'2018':'ImpovRiskPercent'},inplace=True)
exclude_codes=['WLD', 'LAC', 'LCN', 'NAC', 'TLA', 'CEB', 'ECA', 'ECS', 'EU', 'TEC', 'EAP', 'EAS', 'SAS', 'TEA', 'TSA', 'MEA', 'MNA', 'SSA', 'SSF', 'TMN', 'TSS', 'ZAF', 'AFE', 'AFW', 'CAF']
impov=impov[~impov['Country Code'].isin(exclude_codes)]
impov.drop('Country Code',axis=1,inplace=True)

death=death[['Country Name','2018']]
death=death[~death['2018'].isna()]
death.rename(columns={'2018':'DeathRate'},inplace=True)

impov_death_merged=impov.merge(death,how="inner",on="Country Name")
impov_death_merged['ImpovRiskPercent']=pd.to_numeric(impov_death_merged["ImpovRiskPercent"])
impov_death_merged['DeathRate']=pd.to_numeric(impov_death_merged["DeathRate"])
#--------------------------------------------------------------------------------------------------------------------------------------------
### Plotting ###
x=impov_death_merged['ImpovRiskPercent']
y=impov_death_merged['DeathRate']

# Line of best fit
m,b=np.polyfit(x,y,1)
plt.plot(x, m*x + b,color="black")

# R^2
correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

# Plot
plt.scatter(x,y)
plt.xlabel("Risk of Impoverishing Expenditures (%)")
plt.ylabel("Death Rate, Crude (per 1000 people)")
plt.title("Death Rate vs Risk of Impoverishing Expenditures for Surgical Care")
plt.text(38, 2, f"y = {round(m,4)}x + {round(b,2)},  $r^2$ = {round(r_squared,2)}", fontsize = 12)
plt.show()