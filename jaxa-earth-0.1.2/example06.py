
# Load module
from jaxa.earth import je

# Set query parameters
kw_d = ["swr","half-monthly-normal"]
dlim = ["2021-01-01T00:00:00","2021-12-31T00:00:00"]
bbox = [120,20,150,50]
ppu  = 10

# Get information of collections,bands for data
collections,bands = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw_d)

# Get an image for data
data = je.ImageCollection(collection=collections[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution(ppu=ppu)\
           .filter_bounds(bbox=bbox)\
           .select(band=bands[0][0])\
           .get_images()

# Process and show an image
img = je.ImageProcess(data)\
        .calc_spatial_stats()\
        .show_spatial_stats()
