
import rasterio
import pickle
from rasterio.windows import Window
import numpy as np
import geopandas as gpd

def RandomLandCoordPopWeighted():
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

        # Weighted random choice directcly
        idx = np.random.choice(len(flat), p=flat/flat.sum())
        row, col = divmod(idx, dataset.width)
        lat, lon = dataset.xy(row, col)
        print("Coordinates: ", lon, lat)
        print("Done with pop weighted coords")

def main():
    coords = RandomLandCoordPopWeighted()
    print("Coordinates main: ")
    print(coords)

if __name__ == "__main__":
    main()