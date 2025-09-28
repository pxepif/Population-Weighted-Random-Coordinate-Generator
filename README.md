A working population weighted coordinate generator created by me.

This project generates random coordinates weighted by global population density.

    -PopWeightedRandomCoordsBasic.py – Core logic for generating purely random, population-weighted coordinates.

    -PopWeightedRandomCoords.py – A version I use for a GeoGuessr-style game on a Discord server (includes additional logic such as continent restrictions).

The "ne_10m_admin_0_countries.shp" can be downloaded from https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/

Public Domain.

The 'ppp_2020_1km_Aggregated.tif' can be downloaded from https://hub.worldpop.org/geodata/summary?id=24777

Licensed under Creative Commons Attribution (CC BY 4.0).



Place both of these files in the same directory where you are running the code (or update the paths in the code if stored elsewhere)

Note: the PopWeightedRandomCoords.py file can take up to a minute to generate random coordinates if the random numbers generated make it so the round is population weighted and cannot be in Asia or Africa.
