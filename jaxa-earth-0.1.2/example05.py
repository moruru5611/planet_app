
# Load module
from jaxa.earth import je

# Set query parameters
kw_d = ["SMC","_daily"]
dlim = ["2021-08-01T00:00:00","2021-08-10T00:00:00"]

# Get information of collections,bands for data
collections,bands = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw_d)

# Get an image for data
data = je.ImageCollection(collection=collections[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution()\
           .filter_bounds()\
           .select(band=bands[0][0])\
           .get_images()

# Process and show an image
img = je.ImageProcess(data)\
        .calc_temporal_stats("mean")\
        .show_images()
