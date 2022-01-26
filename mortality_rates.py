#
# mortality_rates.py
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import datetime
# import math

# Reads csv file with mortality numbers into Pandas dataframes
fname_mort = 'OGD_gest_kalwo_alter_GEST_KALWOCHE_5J_100.csv'
morttables_df = pd.read_csv(fname_mort, delimiter=';') # semicolon separator instead of comma

# totals per calendar week
mortality_temp_df = morttables_df.groupby(['C-KALWOCHE-0']).sum().reset_index()

# totals per sex and calendar week
mortality_sex_temp_df = morttables_df.groupby(['C-C11-0', 'C-KALWOCHE-0']).sum().reset_index()

# Adds a column with calendar years
# all
mortality_temp_df['Calyear'] = 0
for i in range(mortality_temp_df.shape[0]):
    calyear = int(mortality_temp_df.loc[i, 'C-KALWOCHE-0'][5:9])
    mortality_temp_df.loc[i, 'Calyear'] = calyear
# sex
mortality_sex_temp_df['Calyear'] = 0
for i in range(mortality_sex_temp_df.shape[0]):
    calyear = int(mortality_sex_temp_df.loc[i, 'C-KALWOCHE-0'][5:9])
    mortality_sex_temp_df.loc[i, 'Calyear'] = calyear

# Mortality numbers per calendar year, saves result to csv file
# all
mortality_year_df = mortality_temp_df.groupby(['Calyear']).sum().reset_index()
mortality_year_df.rename(columns = {'F-ANZ-1':'Deaths'}, inplace = True)
mortality_year_df = mortality_year_df[mortality_year_df.Calyear > 2001].reset_index()
mortality_year_df = mortality_year_df.drop(columns = ['index'])
mortality_year_df.to_csv('mortality_by_year.csv', sep = ';', index = False)
# (semicolon separator instead of comma)
# sex
mortality_sex_year_df = mortality_sex_temp_df.groupby(['C-C11-0', 'Calyear']).sum().reset_index()
mortality_sex_year_df.loc[mortality_sex_year_df['C-C11-0'] == 'C11-1', 'C-C11-0'] = 'male'
mortality_sex_year_df.loc[mortality_sex_year_df['C-C11-0'] == 'C11-2', 'C-C11-0'] = 'female'
mortality_sex_year_df.rename(columns = {'C-C11-0':'Sex', 'F-ANZ-1':'Deaths'}, inplace = True)
mortality_sex_year_df = mortality_sex_year_df[mortality_sex_year_df.Calyear > 2001].reset_index()
mortality_sex_year_df = mortality_sex_year_df.drop(columns = ['index'])
mortality_sex_year_df.to_csv('mortality_sex_year_df.csv', sep = ';', index = False)
# (semicolon separator instead of comma)

# Combines mortality data for all, male and female into one Dataframe and csv file
mortality_year_df['Sex'] = 'all'
mortality_df = pd.concat([mortality_year_df,mortality_sex_year_df]).reset_index()
mortality_df = mortality_df.drop(columns = ['index'])
mortality_df.to_csv('mortality_df.csv', sep = ';', index = False)
# (semicolon separator instead of comma)


# Reads csv files with population numbers per year into Pandas dataframes
# and adds calendar year to each file
fname_pop2002 = 'OGD_bevstandjbab2002_BevStand_2002.csv'
pop2002_df = pd.read_csv(fname_pop2002, delimiter=';')
pop2002_df['Calyear'] = 2002
fname_pop2003 = 'OGD_bevstandjbab2002_BevStand_2003.csv'
pop2003_df = pd.read_csv(fname_pop2003, delimiter=';')
pop2003_df['Calyear'] = 2003
fname_pop2004 = 'OGD_bevstandjbab2002_BevStand_2004.csv'
pop2004_df = pd.read_csv(fname_pop2004, delimiter=';')
pop2004_df['Calyear'] = 2004
fname_pop2005 = 'OGD_bevstandjbab2002_BevStand_2005.csv'
pop2005_df = pd.read_csv(fname_pop2005, delimiter=';')
pop2005_df['Calyear'] = 2005
fname_pop2006 = 'OGD_bevstandjbab2002_BevStand_2006.csv'
pop2006_df = pd.read_csv(fname_pop2006, delimiter=';')
pop2006_df['Calyear'] = 2006
fname_pop2007 = 'OGD_bevstandjbab2002_BevStand_2007.csv'
pop2007_df = pd.read_csv(fname_pop2007, delimiter=';')
pop2007_df['Calyear'] = 2007
fname_pop2008 = 'OGD_bevstandjbab2002_BevStand_2008.csv'
pop2008_df = pd.read_csv(fname_pop2008, delimiter=';')
pop2008_df['Calyear'] = 2008
fname_pop2009 = 'OGD_bevstandjbab2002_BevStand_2009.csv'
pop2009_df = pd.read_csv(fname_pop2009, delimiter=';')
pop2009_df['Calyear'] = 2009
fname_pop2010 = 'OGD_bevstandjbab2002_BevStand_2010.csv'
pop2010_df = pd.read_csv(fname_pop2010, delimiter=';')
pop2010_df['Calyear'] = 2010
fname_pop2011 = 'OGD_bevstandjbab2002_BevStand_2011.csv'
pop2011_df = pd.read_csv(fname_pop2011, delimiter=';')
pop2011_df['Calyear'] = 2011
fname_pop2012 = 'OGD_bevstandjbab2002_BevStand_2012.csv'
pop2012_df = pd.read_csv(fname_pop2012, delimiter=';')
pop2012_df['Calyear'] = 2012
fname_pop2013 = 'OGD_bevstandjbab2002_BevStand_2013.csv'
pop2013_df = pd.read_csv(fname_pop2013, delimiter=';')
pop2013_df['Calyear'] = 2013
fname_pop2014 = 'OGD_bevstandjbab2002_BevStand_2014.csv'
pop2014_df = pd.read_csv(fname_pop2014, delimiter=';')
pop2014_df['Calyear'] = 2014
fname_pop2015 = 'OGD_bevstandjbab2002_BevStand_2015.csv'
pop2015_df = pd.read_csv(fname_pop2015, delimiter=';')
pop2015_df['Calyear'] = 2015
fname_pop2016 = 'OGD_bevstandjbab2002_BevStand_2016.csv'
pop2016_df = pd.read_csv(fname_pop2016, delimiter=';')
pop2016_df['Calyear'] = 2016
fname_pop2017 = 'OGD_bevstandjbab2002_BevStand_2017.csv'
pop2017_df = pd.read_csv(fname_pop2017, delimiter=';')
pop2017_df['Calyear'] = 2017
fname_pop2018 = 'OGD_bevstandjbab2002_BevStand_2018.csv'
pop2018_df = pd.read_csv(fname_pop2018, delimiter=';')
pop2018_df['Calyear'] = 2018
fname_pop2019 = 'OGD_bevstandjbab2002_BevStand_2019.csv'
pop2019_df = pd.read_csv(fname_pop2019, delimiter=';')
pop2019_df['Calyear'] = 2019
fname_pop2020 = 'OGD_bevstandjbab2002_BevStand_2020.csv'
pop2020_df = pd.read_csv(fname_pop2020, delimiter=';')
pop2020_df['Calyear'] = 2020
fname_pop2021 = 'OGD_bevstandjbab2002_BevStand_2021.csv'
pop2021_df = pd.read_csv(fname_pop2021, delimiter=';')
pop2021_df['Calyear'] = 2021

# Combines annual population data into one dataframe
population_data_df = pd.concat([pop2002_df,pop2003_df, pop2004_df, pop2005_df, pop2006_df, \
        pop2007_df, pop2008_df, pop2009_df, pop2010_df, pop2011_df, pop2012_df, pop2013_df, \
        pop2014_df, pop2015_df, pop2016_df, pop2017_df, pop2018_df, pop2019_df, pop2020_df, pop2021_df])

# Aggregates numbers by calendar year, save results to csv file
population_year_df = population_data_df.groupby(['Calyear']).sum(['F-ISIS-1']).reset_index()
population_year_df.rename(columns = {'F-ISIS-1':'Population'}, inplace = True)
population_year_df.to_csv('population_by_year.csv', sep = ';', index = False)

# Aggregates numbers by sex and calendar year, save results to csv file
population_sex_year_df = population_data_df.groupby(['C-C11-0', 'Calyear']).sum(['F-ISIS-1']).reset_index()
population_sex_year_df.loc[population_sex_year_df['C-C11-0'] == 'C11-1', 'C-C11-0'] = 'male'
population_sex_year_df.loc[population_sex_year_df['C-C11-0'] == 'C11-2', 'C-C11-0'] = 'female'
population_sex_year_df.rename(columns = {'C-C11-0':'Sex', 'F-ISIS-1':'Population'}, inplace = True)
population_sex_year_df.to_csv('population_by_sex_year.csv', sep = ';', index = False)

# Combines population data for all, male and female into one Dataframe and csv file
population_year_df['Sex'] = 'all'
population_df = pd.concat([population_year_df, population_sex_year_df]).reset_index()
population_df = population_df.drop(columns = ['index'])
population_df.to_csv('population_df.csv', sep = ';', index = False)


# Calulates relative mortality per 100,000 population
rel_mortality_df = pd.DataFrame({'Sex': pd.Series(dtype='object'), 'Year': pd.Series(dtype='int64'),
                   'Mortality': pd.Series(dtype='int64')})
for i in range(mortality_df.shape[0]):
    sex = mortality_df.loc[i, 'Sex']
    calyear = mortality_df.loc[i, 'Calyear']
    deathrate = round(mortality_df.loc[i, 'Deaths'] / population_df.loc[i, 'Population'] * 100000)
    rel_mortality_df.loc[i] = [sex, calyear, deathrate]
rel_mortality_df.to_csv('rel_mortality_df.csv', decimal = ',', sep = ';', index = False)

calculated = 'done' # dummy variable as a signal to the calling program that work is finished
