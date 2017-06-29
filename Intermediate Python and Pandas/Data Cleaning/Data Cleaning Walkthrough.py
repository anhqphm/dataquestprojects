#Import files and datasets

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    key_name = f.replace(".csv","")
    data[key_name] = d 

all_survey = pd.read_csv('schools/survey_all.txt', delimiter ='\t', encoding = 'windows-1252')
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter = '\t', encoding = 'windows-1252')
survey = pd.concat([all_survey, d75_survey], axis = 0)
print(survey.head(5))


survey['DBN'] = survey['dbn']
survey = survey.loc[:,["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]]

data['survey'] = survey
print(data['survey'].shape)

#Extracting Latitude and Longtitude
import re

def find_lat(string):
    r = re.findall('\(.+\)',string)
    r = r[0].split(',')[0].replace('(','')
                                  
    return r

data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(find_lat)

print(data['hs_directory'].head())

def find_lon(string):
    r = re.findall('\(.+\)', string)
    r = r[0].split(',')[1].replace(')','')
    return r

data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(find_lon)

data['hs_directory']['lat']= pd.to_numeric(data['hs_directory']['lat'], errors = 'coerce')

data['hs_directory']['lon']= pd.to_numeric(data['hs_directory']['lon'], errors = 'coerce')

print(data['hs_directory'].head())
