import pandas as pd
import geopandas as pg

busroutes = pd.read_csv('bus-sequences.csv')

busroutes = pg.GeoDataFrame(busroutes)

busroutes['\ufeffRoute']

h13 = busroutes[busroutes['\ufeffRoute'] == 'H13']


#one way
h13[h13['Run'] == 1][['Sequence','Stop_Name','Location_Easting','Location_Northing']]