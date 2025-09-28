import rasterio
import numpy as np
import pickle

with rasterio.open('ppp_2020_1km_Aggregated.tif') as src:

    print(src.bounds)
    print(src.crs)
    
    # Read the data and force it into a float64 array to prevent overflow
    # A float64 array is created and passed to the 'out' parameter
    out_array = np.zeros((src.height, src.width), dtype=np.float64)
    pop = src.read(1, out=out_array)
    pop = np.nan_to_num(pop, nan=0)
    pop_flat = pop.flatten() #takes multi d array and turns it into 1d array
    mask = pop_flat > 0
    pop_nonzero = pop_flat[mask]
    cum_pop = np.cumsum(pop_nonzero, dtype=np.int64)
    total_pop = np.sum(pop_nonzero, dtype=np.int64)
    print(f"The total population is: {total_pop:,.0f}")
    with open("cum_pop_pickle.pkl", "wb") as f:
        pickle.dump((cum_pop, np.where(mask)[0]), f)


