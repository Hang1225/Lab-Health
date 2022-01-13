########## Questions ##########

# 1. How does the life expectancy of male vs female change in Asia and North America from 1960-2019?
# 2. How does the risk of impoverishing expenditures for surgical care correlate to the death rate per 1000 people in 2018? Reach: all the 2009-2018 data?
# 3. Does percentage of births attended by skilled health staff affect maternal mortality rate? Does it vary by continent and by country??
# 4. How does the % of pregnant women recieving prenatal care compare to the infant mortality rate?

########## Data Sources ##########

# 1. Life expectancy at birth, male: https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN?view=chart
# 1. Life expectancy at birth, female: https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?view=chart
# 2a. Risk of impoverishing expenditures: https://data.worldbank.org/indicator/SH.SGR.IRSK.ZS?view=chart
# 2b. Death Rate, Crude (per 1000 people): https://data.worldbank.org/indicator/SP.DYN.CDRT.IN?view=chart 
# 3. Births attended by skilled health staff (% of total): https://data.worldbank.org/indicator/SH.STA.BRTC.ZS?view=chart
# 3. Maternal mortality ratio (modeled estimate, per 100,000 live births): https://data.worldbank.org/indicator/SH.STA.MMRT?end=2010&start=2010&view=chart
# 4. Pregnant women recieving prenatal care (%): https://data.worldbank.org/indicator/SH.STA.ANVC.ZS?view=chart
# 4. Mortality rate, infant (per 1,000 live births): https://data.worldbank.org/indicator/SP.DYN.IMRT.IN?view=chart
# country-to-continent.csv: https://gist.github.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c
    # bridge dataset to link country to their respective continent

########## Extraction ##########

# Download the .CSV found on each of the webpages

# ==========
# Question 1
# Read in Life_Expectancy_Male.csv and Life_Expectancy_Female.csv using pd.read_csv and store them in separate variables.

# ==========
# Question 2
# Using pd.read_csv, read in both .csv files as separate pandas DataFrames.
    # Skip the first 4 rows using the parameter, skiprows = 4.
    
# ==========
# Question 3
# 1. Read in csv files for Births attended by skilled health staff, Maternal mortality ratio, and country to continent
# 2. When reading in files, skip 3 rows (except for the continent to country csv).
# 3. Store each csv file in a memorable variable.

# ==========
# Question 4
# Read in the csv files for Pregnant women receiving prenatal care, and Mortality rate, infant (per 1,000 live births)
# Skip the first 4 rows using the parameter, skiprows = 4.

# Store each csv in separate variables.

########## Transformation ##########

# 1.
    # Drop unnecessary columns using Dataframe.drop(), pass in the columns: ‘Indicator Name’, ‘Indicator Code’, ‘2020’, ‘Unnamed: 65’ as a list. Set ‘axis’ parameter to 1 and ‘inplace’ to True.
    # Drop empty rows using Dataframe.dropna() to drop the empty rows. Set ‘inplace’ to True.
    # Filter the data for East Asia & Pacific by filtering out the row where Country Code = 'EAS', store this data in a separate variable.
    # Filter the data for North America by filtering out the row where Country Code = 'NAC', store this data in a separate variable.
    # (Do the above steps for both male and female dataset)
    # To extract values from Dataframe for plotting visualizations, index with [2:] to eliminate the first two columns (Country Name, Country Code).
     
# 2. How does the risk of impoverishing expenditures for surgical care correlate to the death rate per 1000 people in 2018?
    # 2a. Risk of impoverishing expenditures
        # Drop all colunns besides '2018', 'Country Name', 'Country Code' 
        # Change '2018' column name to 'ImpovRiskPercent'
        # Remove rows with NaN in 'ImpovRiskPercent'
        # Remove rows with 'Country Code' = ['WLD', 'LAC', 'LCN', 'NAC', 'TLA', 'CEB', 'ECA', 'ECS', 'EU', 'TEC', 'EAP', 'EAS', 'SAS', 'TEA', 'TSA', 'MEA', 'MNA', 'SSA', 'SSF', 'TMN', 'TSS', 'ZAF', 'AFE', 'AFW', 'CAF']
            # Those are aggregated countries like North America, etc.
        # Remove 'Country Code' column
    # 2b. Death Rate, Crude (per 1000 people)
        # Drop all colunns besides '2018', 'Country Name'
        # Change '2018' column name to 'DeathRate'
        # Remove any rows with NaN values in 'DeathRate'
        # Merge 2a and 2b into a single DataFrame (on="Country Name", how="inner")
        # Convert 'ImpovRiskPercent' and 'DeathRate' columns to numeric

# 3. 
    # For country to continent csv: drop all columns except for three letter country code, continent name, and country name
    # For 2 WorldBank Sources: 
        # Remove all columns except for 2017 and country code.
            # You may want to keep country name in one of the dataframes for merging/visualization readability.
        # Include an indicator of what the data is from in the 2017 column name. (i.e.'2017-mmr', etc.)
        # Remove rows with 'Country Code' = ['WLD', 'LAC', 'LCN', 'NAC', 'TLA', 'CEB', 'ECA', 'ECS', 'EU', 'TEC', 'EAP', 'EAS', 'SAS', 'TEA', 'TSA', 'MEA', 'MNA', 'SSA', 'SSF', 'TMN', 'TSS', 'ZAF', 'AFE', 'AFW', 'CAF']
            # Those are aggregated countries like North America, etc.
        # Remove rows with null values.
    # Merge Worldbank dataframes along country code(not the country to continent table).
    # Using the large merged dataframes, add the country to continent csv file by merging(country code to three letter country code).
    # Group by continent to compare both maternal mortality rates and births attended by skilled healthcare workers. Is there a relationship?
    # Select one continent and see if the countries within that continent vary. Have fun with it!

# 4. To compare the prenatal care percentages to infant mortality, use all data collected in 2000 across various countries.
    # Remove rows with 'Country Code' = ['WLD', 'LAC', 'LCN', 'NAC', 'TLA', 'CEB', 'ECA', 'ECS', 'EU', 'TEC', 'EAP', 'EAS', 'SAS', 'TEA', 'TSA', 'MEA', 'MNA', 'SSA', 'SSF', 'TMN', 'TSS', 'ZAF', 'AFE', 'AFW', 'CAF']
        # Those are aggregated countries like North America, etc.
    # Filter both prenatal care dataframe and infant mortality dataframe for "Country Name" and "2000".
    # Rename 2000 column in both dataframes to reflect dataset - Prenatal care or Infant Mortality.
    # Remove rows that are empty in the "2000" column - meaning they are missing Prenatal or Mortality data.
    # Inner merge DataFrames on "Country Name".

########## Load ##########