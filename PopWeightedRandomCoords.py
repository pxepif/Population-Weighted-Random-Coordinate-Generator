import random
import math
import rasterio
import pickle
from rasterio.windows import Window
import time
import multiprocessing
import numpy as np
import certifi
import ssl
import os
import datetime
from shapely.geometry import Point, shape
import geopandas as gpd
from global_land_mask import globe

def popWeighted():
    with open("cum_pop_pickle.pkl", "rb") as infile:
            cum_pop, populated_indices = pickle.load(infile) #population of all cells combined via python's negative indexing

    with rasterio.open('ppp_2020_1km_Aggregated.tif') as dataset:

        # Create the output array with the desired data type (float64) and dimensions.
        out_array = np.zeros((dataset.height, dataset.width), dtype=np.float64)
        
        
        # This line reads the data from the file and writes it into the out_array,
        # converting the data type to float64 in the process.
        data = dataset.read(1, out=out_array)
    
        total_pop = cum_pop[-1]
        print(total_pop)

        random_pop = np.random.uniform(0, total_pop)
        print(random_pop)
        row = np.searchsorted(cum_pop, random_pop)
        print(cum_pop[row-1], cum_pop[row])
        full_raster_flat = data.flatten()
        flat = data.flatten()
        flat[flat < 0] = 0

        r_number2 = random.random()
        print("Rnumber2: ", r_number2)
        if r_number2 < 0.5:
            print("Round must be in the Americas, Europe, or Oceania")
            continents = gpd.read_file("ne_10m_admin_0_countries.shp")

            while True:
                check = False
                idx = np.random.choice(len(flat), p=flat/flat.sum())
                row, col = divmod(idx, dataset.width)
                lon, lat = dataset.xy(row, col)
                print("Lat, lon: ", lat, lon)
                pt = Point(lon, lat) #continents.iterrows goes thru every country in the file
                for _, row in continents.iterrows():
                    if (row["CONTINENT"] == "Asia" and row["geometry"].contains(pt) or 
                    row["CONTINENT"] == "Africa" and row["geometry"].contains(pt)):
                        print("Rerolling due to Asia/Africa")
                        check=False
                        #break
                    elif row["geometry"].contains(pt):
                        check = True
                        break
                #end for
                if check:
                    print("Coordinates: ", lat, ", ", lon)
                    break
                else:
                    continue
            #end while
        else:
            # Weighted random choice directcly
            idx = np.random.choice(len(flat), p=flat/flat.sum())
            row, col = divmod(idx, dataset.width)
            lat, lon = dataset.xy(row, col)
            print("Coordinates: ", lon, lat)
            print("Done with pop weighted coords")

def notPopWeighted():
    while True:
            u = random.uniform(0, 1)
            lat = math.degrees(math.asin(2 * u - 1))  # arcsin(-1 to 1) → lat in degrees
            lon = random.uniform(-180, 180)
            print(lat)
            print(lon)
            if (globe.is_land(lat, lon)): #and lat > -60: (antarctica is eligible now)
                return (lat, lon)

def RandomLandCoord():

    r_number = random.random()
    print("Rnumber: ", r_number)
    if r_number < 0.99:
        coords = popWeighted()
        return coords
    else:
        coords = notPopWeighted()
        return coords

def main():
    coords = RandomLandCoord()
    print("Coordinates main: ")
    print(coords)

if __name__ == "__main__":
    main()