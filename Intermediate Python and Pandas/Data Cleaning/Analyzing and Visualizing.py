correlations = combined.corr()
correlations = correlations['sat_score']
print(correlations)

import matplotlib.pyplot as plt

combined.plot.scatter(x = 'total_enrollment', y='sat_score')

plt.show()


low_enrollment = combined[(combined['total_enrollment'] < 1000) & (combined['sat_score'] < 1000)]

print(low_enrollment['School Name'])


combined.plot.scatter(x = 'ell_percent', y='sat_score')
plt.show()

#Creating map

from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longtitudes = combined['lon'].tolist()
latitudes = combined['lat'].tolist()

m.scatter(longtitudes, latitudes, s=20, zorder=2,latlon=True, c = combined['ell_percent'], cmap = 'summer')

plt.show()



