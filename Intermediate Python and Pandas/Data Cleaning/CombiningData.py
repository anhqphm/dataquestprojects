
class_size = data['class_size']
class_size = class_size[class_size['GRADE '] == '09-12']
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']

print(class_size.head(5))

import numpy

class_size = class_size.groupby('DBN').agg(numpy.mean)

class_size.reset_index(inplace = True)

data['class_size'] = class_size

print(data['class_size'].head())

data['graduation'] = data['graduation'][data['graduation']['Cohort'] == '2006']
data['graduation'] = data['graduation'][data['graduation']['Demographic'] == 'Total Cohort']
print(data['graduation'].head())


cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for each in cols:
    data['ap_2010'][each] = pd.to_numeric(data['ap_2010'][each], errors = 'coerce')
    
print(data['ap_2010'].head())
                                          
  
combined = data["sat_results"]

combined = combined.merge(data['ap_2010'],on='DBN', how ='left')
combined = combined.merge(data['graduation'], on='DBN', how ='left')

print(combined.head())
print(combined.shape)

cols = ['class_size','demographics', 'survey', 'hs_directory']
for each in cols: 
    combined = combined.merge(data[each], on='DBN', how='inner')

print(combined.head())
print(combined.shape)

means = combined.mean()
combined = combined.fillna(means)
combined = combined.fillna(0)

print(combined.head())

def schooldistrict(dbn):
    return dbn[0:2]

combined['school_dist'] = combined['DBN'].apply(schooldistrict)

print(combined['school_dist'].head())
    
    
