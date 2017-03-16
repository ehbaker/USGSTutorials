#Import external libraries
from shapely.geometry import Point, LineString
import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
#Steps to create lines from points dataframe
#Read in lat/lon data
data=pd.read_csv(r"Q:\Project Data\GlacierData\GPR\Wolverine\2016\exported_data\GPSTracePoints_LatLon_Wolverine_2016.csv")
#Make points
df = pd.DataFrame(data)
geometry = [Point(xy) for xy in zip(df['Lon'], df['Lat'])]
gdf = GeoDataFrame(df, geometry=geometry)
gdf.crs = {'init' :'epsg:4326'} # this is WGS84, projection for lat/lon points.

#Make dataframe of lines
LineSeries = df.groupby(['Directory'])['geometry'].apply(lambda x: LineString(x.tolist()))
dfLine = GeoDataFrame(LineSeries, geometry='geometry')

dfLine.to_file("LinesforWolv2016") #saves file in a directory with given name
