import pandas as pd
import geopandas as pg
import pyproj
from shapely.geometry import LineString, Point
import matplotlib.pyplot as plt


bng = pyproj.Proj(init='epsg:27700')
wgs84 = pyproj.Proj(init='epsg:4326')


crs = {'init':'epsg:4326'} 
busroutes = pd.read_csv('bus-sequences.csv', skipfooter=1)
busroutes = busroutes.ix[:55931] #reomve the NaN row at the end
# need to convert Eastings and Northing to coordinates first

geometry = []

for row in busroutes.itertuples(): #Location_Easting = index[8], Location_Northing[9]
	lon, lat = pyproj.transform(bng, wgs84, row[8], row[9])
	point = Point(lon, lat)
	geometry.append(point)


busroutes = pg.GeoDataFrame(busroutes, crs=crs, geometry=geometry)




busroutes.to_crs(epsg=4326)  #delete?


h13 = busroutes[busroutes['\ufeffRoute'] == 'H13']



h13_out = h13[h13['Run'] == 1]


h13_out_start = h13_out[h13_out.Sequence == 1].geometry 
h13_out_end = h13_out[h13_out.Sequence == 38].geometry  
h13[h13['Run'] == 1][['Sequence']].max() #to find last number in sequence of bus stops


line = []                                                             
for row in h13_out.itertuples():
     line.append(row.geometry)

h13_route = LineString(line)

h13_route.length # = 0.13353557348356146

h13_out_start.get_values()[0].distance(h13_out_end.get_values()[0]) # = 0.015038338777859562

"""
HOw to add this in as columns
"""
